-- ============================================
-- File: 02_basic_queries.sql
-- Purpose: Basic business analysis
-- ============================================

-- Q1: City wise customers
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC;

-- Q2: Loyalty tier distribution with percentage
SELECT 
    loyalty_tier, 
    COUNT(*) AS customers,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM customers
GROUP BY loyalty_tier
ORDER BY customers DESC;

-- Q3: Recent orders with customer details
SELECT 
    o.order_id, c.name AS customer, c.city, 
    o.order_date, o.order_status, o.payment_method
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC
LIMIT 20;

-- Q4: Top 10 highest value orders
SELECT 
    oi.order_id,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)), 2) AS order_revenue
FROM order_items oi
GROUP BY oi.order_id
ORDER BY order_revenue DESC
LIMIT 10;

-- Q5: Top 10 best-selling products
SELECT 
    p.product_name, p.category, p.brand,
    SUM(oi.quantity) AS total_sold,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)), 2) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.brand
ORDER BY total_sold DESC
LIMIT 10;

-- Q6: Category wise revenue
SELECT 
    p.category,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)), 2) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- Q7: Top 10 sellers by revenue
SELECT 
    s.seller_name, s.city, s.rating,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)), 2) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN sellers s ON p.seller_id = s.seller_id
GROUP BY s.seller_id, s.seller_name, s.city, s.rating
ORDER BY revenue DESC
LIMIT 10;

-- Q8: Average Order Value by city
SELECT 
    c.city,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct/100.0)) / 
          COUNT(DISTINCT o.order_id), 2) AS avg_order_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.order_status = 'Delivered'
GROUP BY c.city
ORDER BY avg_order_value DESC;

-- Q9: Payment methods
SELECT 
    payment_method,
    COUNT(*) AS total_orders,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM orders
GROUP BY payment_method
ORDER BY total_orders DESC;

-- Q10: Order status breakdown
SELECT 
    order_status,
    COUNT(*) AS total_orders,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;