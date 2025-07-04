-- C:\Users\ginnu\Projects\airflow-docker\dbt_project\sales_analytics\models\marts\fact_sales.sql

SELECT
    s.order_id,
    dd.date_key AS order_date_key,
    dp.product_key,
    s.quantity_ordered,
    s.price_each,
    s.cost_price,
    s.turnover,
    s.margin,
    (s.quantity_ordered * s.cost_price) AS total_cost,
    (s.turnover - (s.quantity_ordered * s.cost_price)) AS total_profit
FROM {{ ref('stg_sales') }} s
JOIN {{ ref('dim_dates') }} dd ON TO_CHAR(s.order_date, 'YYYYMMDD')::INT = dd.date_key
JOIN {{ ref('dim_products') }} dp ON s.product_ean = dp.product_ean AND s.product_name = dp.product_name AND s.product_category = dp.product_category
-- Removed the JOIN to dim_addresses as it's not being created at this time.