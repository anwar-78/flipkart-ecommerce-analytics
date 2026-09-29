-- ============================================
-- File: 03_funnel_analysis.sql
-- Purpose: User journey drop-off analysis
-- ============================================

-- Funnel stages
SELECT 
    event_type,
    COUNT(*) AS total_events,
    COUNT(DISTINCT customer_id) AS unique_users
FROM events
GROUP BY event_type
ORDER BY total_events DESC;

-- Conversion rates
SELECT
    COUNT(*) FILTER (WHERE event_type='view') AS views,
    COUNT(*) FILTER (WHERE event_type='add_to_cart') AS carts,
    COUNT(*) FILTER (WHERE event_type='purchase') AS purchases,
    ROUND(100.0 * COUNT(*) FILTER (WHERE event_type='add_to_cart') / 
          NULLIF(COUNT(*) FILTER (WHERE event_type='view'),0), 2) AS view_to_cart_pct,
    ROUND(100.0 * COUNT(*) FILTER (WHERE event_type='purchase') / 
          NULLIF(COUNT(*) FILTER (WHERE event_type='add_to_cart'),0), 2) AS cart_to_purchase_pct,
    ROUND(100.0 * COUNT(*) FILTER (WHERE event_type='purchase') / 
          NULLIF(COUNT(*) FILTER (WHERE event_type='view'),0), 2) AS overall_conversion_pct
FROM events;