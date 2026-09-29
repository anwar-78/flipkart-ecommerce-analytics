-- ============================================
-- File: 06_delivery_analysis.sql
-- Purpose: Delivery partner performance
-- ============================================

SELECT 
    delivery_partner,
    COUNT(*) AS total_deliveries,
    ROUND(AVG(delivery_date - dispatch_date), 1) AS avg_delivery_days,
    COUNT(*) FILTER (WHERE delivery_status='Returned') AS returned,
    ROUND(100.0 * COUNT(*) FILTER (WHERE delivery_status='Returned') / COUNT(*), 2) AS return_pct
FROM delivery
GROUP BY delivery_partner
ORDER BY return_pct DESC;