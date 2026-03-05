-- Create database
CREATE DATABASE IF NOT EXISTS atliq_tshirts;
USE atliq_tshirts;

-- T-shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT PRIMARY KEY AUTO_INCREMENT,
    brand VARCHAR(50) NOT NULL,
    color VARCHAR(30) NOT NULL,
    size VARCHAR(5) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Discounts table
CREATE TABLE discounts (
    discount_id INT PRIMARY KEY AUTO_INCREMENT,
    t_shirt_id INT,
    pct_discount DECIMAL(5,2),
    FOREIGN KEY (t_shirt_id) REFERENCES t_shirts(t_shirt_id)
);

-- Sample data for t_shirts
INSERT INTO t_shirts (brand, color, size, price, stock_quantity) VALUES
('Nike', 'White', 'XS', 29.99, 45),
('Nike', 'White', 'S', 29.99, 52),
('Nike', 'White', 'M', 29.99, 68),
('Nike', 'White', 'L', 29.99, 72),
('Nike', 'White', 'XL', 29.99, 50),
('Nike', 'Black', 'XS', 32.99, 35),
('Nike', 'Black', 'S', 32.99, 40),
('Nike', 'Black', 'M', 32.99, 55),
('Nike', 'Black', 'L', 32.99, 60),
('Nike', 'Black', 'XL', 32.99, 45),
('Adidas', 'White', 'XS', 27.99, 50),
('Adidas', 'White', 'S', 27.99, 58),
('Adidas', 'White', 'M', 27.99, 75),
('Adidas', 'White', 'L', 27.99, 80),
('Adidas', 'White', 'XL', 27.99, 55),
('Adidas', 'Blue', 'XS', 30.99, 40),
('Adidas', 'Blue', 'S', 30.99, 48),
('Adidas', 'Blue', 'M', 30.99, 62),
('Adidas', 'Blue', 'L', 30.99, 70),
('Adidas', 'Blue', 'XL', 30.99, 50),
('Levi', 'White', 'XS', 35.99, 55),
('Levi', 'White', 'S', 35.99, 65),
('Levi', 'White', 'M', 35.99, 85),
('Levi', 'White', 'L', 35.99, 90),
('Levi', 'White', 'XL', 35.99, 60),
('Levi', 'Red', 'XS', 38.99, 30),
('Levi', 'Red', 'S', 38.99, 38),
('Levi', 'Red', 'M', 38.99, 50),
('Levi', 'Red', 'L', 38.99, 55),
('Levi', 'Red', 'XL', 38.99, 40);

-- Sample data for discounts
INSERT INTO discounts (t_shirt_id, pct_discount) VALUES
(1, 10.00),
(6, 15.00),
(11, 5.00),
(16, 20.00),
(21, 8.00),
(26, 12.00);
