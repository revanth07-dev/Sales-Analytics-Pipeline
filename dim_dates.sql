-- models/dimensions/dim_dates.sql
SELECT DISTINCT
    TO_CHAR(order_date, 'YYYYMMDD')::INT AS date_key,
    order_date::DATE AS full_date,
    EXTRACT(DAY FROM order_date) AS day_of_month,
    EXTRACT(MONTH FROM order_date) AS month,
    TO_CHAR(order_date, 'Month') AS month_name,
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(QUARTER FROM order_date) AS quarter,
    EXTRACT(DOW FROM order_date) AS day_of_week_num, -- 0=Sunday, 1=Monday etc.
    TO_CHAR(order_date, 'Day') AS day_of_week_name,
    CASE WHEN EXTRACT(DOW FROM order_date) IN (0, 6) THEN TRUE ELSE FALSE END AS is_weekend
FROM {{ ref('stg_sales') }}
WHERE order_date IS NOT NULL