-- ============================================
-- File: 04_cohort_retention.sql
-- Purpose: Customer retention analysis
-- ============================================

WITH first_order AS (
    SELECT 
        customer_id,
        MIN(order_date) AS first_order_date,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
),
monthly_orders AS (
    SELECT 
        o.customer_id,
        DATE_TRUNC('month', o.order_date) AS order_month
    FROM orders o
    GROUP BY o.customer_id, DATE_TRUNC('month', o.order_date)
)
SELECT
    f.cohort_month,
    m.order_month,
    COUNT(DISTINCT m.customer_id) AS active_customers
FROM first_order f
JOIN monthly_orders m ON f.customer_id = m.customer_id
GROUP BY f.cohort_month, m.order_month
ORDER BY f.cohort_month, m.order_month;