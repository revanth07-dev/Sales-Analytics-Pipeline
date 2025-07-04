-- models/dimensions/dim_products.sql
SELECT DISTINCT
    {{ dbt_utils.generate_surrogate_key(['product_ean', 'product_name', 'product_category']) }} AS product_key,
    product_ean,
    product_name,
    product_category
FROM {{ ref('stg_sales') }}
WHERE product_ean IS NOT NULL -- Ensure unique EANs for products