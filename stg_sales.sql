-- C:\Users\ginnu\Projects\airflow-docker\dbt_project\sales_analytics\models\staging\stg_sales.sql

SELECT
    "Order ID"::BIGINT AS order_id,                     -- Cast to BIGINT
    "Order Date"::TIMESTAMP AS order_date,              -- Cast to TIMESTAMP
    "Product"::TEXT AS product_name,                    -- Cast to TEXT
    "Product_ean"::TEXT AS product_ean,                 -- Cast to TEXT
    "catégorie"::TEXT AS product_category,              -- Cast to TEXT
    "Purchase Address"::TEXT AS purchase_address,       -- Cast to TEXT
    "Quantity Ordered"::BIGINT AS quantity_ordered,     -- Cast to BIGINT
    "Price Each"::DOUBLE PRECISION AS price_each,       -- Cast to DOUBLE PRECISION
    "Cost price"::DOUBLE PRECISION AS cost_price,       -- Cast to DOUBLE PRECISION
    turnover::DOUBLE PRECISION AS turnover,             -- Cast to DOUBLE PRECISION
    margin::DOUBLE PRECISION AS margin                  -- Cast to DOUBLE PRECISION

FROM {{ source('sales_raw', 'sales') }}