-- Crear base de datos
CREATE DATABASE IF NOT EXISTS myflaskapp;
USE myflaskapp;

-- =====================
-- Tabla USERS
-- =====================
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
);

-- Datos iniciales de usuarios
INSERT INTO users (name, email, username, password) VALUES
('juan', 'juan@gmail.com', 'juan', '123'),
('maria', 'maria@gmail.com', 'maria', '456');

-- =====================
-- Tabla PRODUCTS
-- =====================
DROP TABLE IF EXISTS products;
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    quantity INT
);

-- Datos iniciales de productos
INSERT INTO products (name, price, quantity) VALUES
('pc', 150, 10),
('phone', 100, 20),
('headphones', 110, 25);

-- =====================
-- Tabla ORDERS
-- =====================
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(255),
    userEmail VARCHAR(255),
    saleTotal DECIMAL(10,2),
    date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Datos iniciales de órdenes (ejemplo)
INSERT INTO orders (userName, userEmail, saleTotal) VALUES
('juan', 'juan@gmail.com', 250.00);

