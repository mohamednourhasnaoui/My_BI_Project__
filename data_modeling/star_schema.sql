
CREATE TABLE Dim_Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    segment VARCHAR(100)
);

CREATE TABLE Dim_Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100)
);

CREATE TABLE Dim_Date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

CREATE TABLE Dim_Region (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(100)
);

CREATE TABLE Fact_Sales (
    sales_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    date_id DATE,
    region_id INT,
    quantity INT,
    total_sales FLOAT
);
