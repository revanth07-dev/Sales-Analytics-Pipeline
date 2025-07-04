from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
import os

DAG_BASE_PATH = os.path.dirname(os.path.abspath(__file__))

with DAG(
    dag_id='sales_data_pipeline_ingestion',
    start_date=datetime(2025, 6, 29),
    schedule_interval='@daily',
    catchup=False,
    tags=['sales', 'etl', 'ingestion'],
    doc_md="""
    ### Sales Data Ingestion DAG

    This DAG loads data from `sales_data.csv` into the `staging.sales` table
    in the PostgreSQL `sales_data_warehouse` database using a Python script.
    """
) as dag:

    ingest_sales_data_task = BashOperator(
        task_id='load_sales_data_to_staging',
        bash_command='python3 /opt/airflow/dags/load_sales_data.py'
    )

    ingest_sales_data_task
