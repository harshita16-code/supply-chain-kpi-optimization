-- SQL Queries for E-Commerce Sales Analysis

-- 1. Create table for orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    Product VARCHAR(50),
    Region VARCHAR(20),
    OrderQuantity INT,
    UnitPrice DECIMAL(10,2),
    OrderDate DATE,
    Revenue DECIMAL(12,2)
);

-- 2. Load data (adjust path if required)
-- For MySQL:
-- LOAD DATA INFILE 'data/raw/orders.csv'
-- INTO TABLE Orders
-- FIELDS TERMINATED BY ','
-- IGNORE 1 ROWS;

-- 3. Top 5 highest revenue-generating products
SELECT Product, SUM(Revenue) AS TotalRevenue
FROM Orders
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 4. Sales by Region
SELECT Region, SUM(Revenue) AS RegionalRevenue
FROM Orders
GROUP BY Region
ORDER BY RegionalRevenue DESC;

-- 5. Monthly sales trend
SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, SUM(Revenue) AS MonthlyRevenue
FROM Orders
GROUP BY Month
ORDER BY Month;

-- 6. Average order value
SELECT AVG(Revenue) AS AvgOrderValue
FROM Orders;

-- 7. Total revenue per product
SELECT Product, SUM(Revenue) AS TotalRevenue, COUNT(*) AS OrdersCount
FROM Orders
GROUP BY Product
ORDER BY TotalRevenue DESC;

-- 8. Identify most sold product
SELECT Product, SUM(OrderQuantity) AS TotalQuantity
FROM Orders
GROUP BY Product
ORDER BY TotalQuantity DESC
LIMIT 1;
