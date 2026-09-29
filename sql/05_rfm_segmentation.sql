-- ============================================
-- File: 05_rfm_segmentation.sql
-- Purpose: Customer segmentation (Recency, Frequency, Monetary)
-- ============================================

WITH customer_rfm AS (
    SELECT 
        c.customer_id,
        c.name,
        MAX(o.order_date) AS last_order_date,
        CURRENT_DATE - MAX(o.order_date) AS recency_days,
        COUNT(DISTINCT o.order_id) AS frequency,
        ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)), 2) AS monetary
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'Delivered'
    GROUP BY c.customer_id, c.name
)
SELECT 
    customer_id, name, recency_days, frequency, monetary,
    CASE
        WHEN recency_days < 90 AND frequency >= 3 AND monetary > 50000 THEN 'Champion'
        WHEN recency_days < 180 AND frequency >= 2 THEN 'Loyal'
        WHEN recency_days BETWEEN 180 AND 365 THEN 'At Risk'
        ELSE 'Lost'
    END AS segment
FROM customer_rfm
ORDER BY monetary DESC;