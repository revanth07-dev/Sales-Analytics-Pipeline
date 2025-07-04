import pandas as pd
from sqlalchemy import create_engine, text
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data_to_staging(csv_file_path, db_connection_str, table_name, schema_name):
    logging.info(f"Starting data loading process for {csv_file_path} into {schema_name}.{table_name}")

    try:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)
        logging.info(f"Successfully read {len(df)} rows from {csv_file_path}")

        # Data type conversions
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        logging.info("Converted 'Order Date' to datetime.")

        df['Product_ean'] = df['Product_ean'].astype(str).str.replace(r'\.0$', '', regex=True)
        logging.info("Converted 'Product_ean' to string.")

        initial_rows = len(df)
        df.dropna(subset=['Order Date'], inplace=True)
        if len(df) < initial_rows:
            logging.warning(f"Dropped {initial_rows - len(df)} rows due to invalid 'Order Date' values.")

        # Create SQLAlchemy engine for Postgres
        engine = create_engine(db_connection_str)
        logging.info("SQLAlchemy engine created.")

        with engine.connect() as conn:
            # Create schema if it doesn't exist
            conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {schema_name}"))
            logging.info(f"Ensured schema '{schema_name}' exists.")

            # Check if table exists
            table_check_sql = text(f"""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = :schema_name AND table_name = :table_name
                )
            """)
            result = conn.execute(table_check_sql, {"schema_name": schema_name, "table_name": table_name})
            table_exists = result.scalar()

            if not table_exists:
                logging.info(f"Table {schema_name}.{table_name} does not exist. Creating and inserting all data.")
                df.to_sql(table_name, conn, if_exists='replace', index=False, schema=schema_name)
                logging.info(f"Inserted {len(df)} rows into {schema_name}.{table_name}")
            else:
                logging.info(f"Table {schema_name}.{table_name} exists. Inserting only new rows.")

                # Load existing data keys from the table (use columns that uniquely identify a row)
                # Assuming 'Order Date' and 'Product_ean' combined uniquely identify a record,
                # modify this if your uniqueness criteria differ.

                existing_keys_query = text(f"""
                    SELECT "Order Date", "Product_ean"
                    FROM {schema_name}.{table_name}
                """)
                existing_keys_df = pd.read_sql(existing_keys_query, conn)

                # Normalize types for comparison
                existing_keys_df['Order Date'] = pd.to_datetime(existing_keys_df['Order Date'], errors='coerce')
                existing_keys_df['Product_ean'] = existing_keys_df['Product_ean'].astype(str)

                # Merge to find new rows
                merged = pd.merge(
                    df, 
                    existing_keys_df, 
                    how='left', 
                    on=['Order Date', 'Product_ean'], 
                    indicator=True
                )
                new_rows = merged[merged['_merge'] == 'left_only'].drop(columns=['_merge'])

                if not new_rows.empty:
                    logging.info(f"Inserting {len(new_rows)} new rows into {schema_name}.{table_name}.")
                    new_rows.to_sql(table_name, conn, if_exists='append', index=False, schema=schema_name)
                else:
                    logging.info("No new rows to insert.")

    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at {csv_file_path}")
    except Exception as e:
        logging.error(f"An error occurred during data loading: {e}", exc_info=True)


if __name__ == "__main__":
    CSV_FILE = "/opt/airflow/dags/sales_data.csv"
    DB_CONNECTION = 'postgresql://user:password@host.docker.internal:5432/sales_data_warehouse'
    TABLE_NAME = 'sales'
    SCHEMA_NAME = 'staging'

    load_data_to_staging(CSV_FILE, DB_CONNECTION, TABLE_NAME, SCHEMA_NAME)
