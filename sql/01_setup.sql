-- ============================================
-- File: 01_setup.sql
-- Purpose: Create tables and import data
-- ============================================

-- ============ TABLES CREATE ============

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50),
    state VARCHAR(50),
    signup_date DATE,
    loyalty_tier VARCHAR(20)
);

CREATE TABLE sellers (
    seller_id VARCHAR(10) PRIMARY KEY,
    seller_name VARCHAR(100),
    city VARCHAR(50),
    rating DECIMAL(3,1),
    join_date DATE
);

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    seller_id VARCHAR(10)
);

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    order_date DATE,
    order_status VARCHAR(20),
    payment_method VARCHAR(30)
);

CREATE TABLE order_items (
    order_item_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_pct INT
);

CREATE TABLE events (
    event_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    session_id VARCHAR(20),
    event_type VARCHAR(20),
    product_id VARCHAR(10),
    event_timestamp TIMESTAMP
);

CREATE TABLE delivery (
    delivery_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    delivery_partner VARCHAR(50),
    dispatch_date DATE,
    delivery_date DATE,
    delivery_status VARCHAR(20),
    delivery_city VARCHAR(50)
);

-- ============ IMPORT DATA ============

COPY customers FROM 'D:/Flipkart Project Data Analytics/data/customers.csv' 
DELIMITER ',' CSV HEADER;

COPY sellers FROM 'D:/Flipkart Project Data Analytics/data/sellers.csv' 
DELIMITER ',' CSV HEADER;

COPY products FROM 'D:/Flipkart Project Data Analytics/data/products.csv' 
DELIMITER ',' CSV HEADER;

COPY orders FROM 'D:/Flipkart Project Data Analytics/data/orders.csv' 
DELIMITER ',' CSV HEADER;

COPY order_items FROM 'D:/Flipkart Project Data Analytics/data/order_items.csv' 
DELIMITER ',' CSV HEADER;

COPY events FROM 'D:/Flipkart Project Data Analytics/data/events.csv' 
DELIMITER ',' CSV HEADER;

COPY delivery FROM 'D:/Flipkart Project Data Analytics/data/delivery.csv' 
DELIMITER ',' CSV HEADER;

-- ============ VERIFY ============

SELECT 'customers' AS table_name, COUNT(*) FROM customers
UNION ALL SELECT 'sellers', COUNT(*) FROM sellers
UNION ALL SELECT 'products', COUNT(*) FROM products
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL SELECT 'events', COUNT(*) FROM events
UNION ALL SELECT 'delivery', COUNT(*) FROM delivery;