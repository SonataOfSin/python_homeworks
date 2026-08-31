
--customers ცხრილი
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

--customer_profiles ცხრილი (One-to-One კავშირი customers-თან)
CREATE TABLE customer_profiles (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    CONSTRAINT fk_customer_profile FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

--suppliers ცხრილი
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(150) NOT NULL UNIQUE
);

--products ცხრილი (One-to-Many კავშირი suppliers-თან)
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    supplier_id INT NOT NULL,
    CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE RESTRICT
);

--orders ცხრილი (One-to-Many კავშირი customers-თან)
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    customer_id INT NOT NULL,
    CONSTRAINT fk_customer_order FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

--order_items შუამავალი ცხრილი (Many-to-Many კავშირი orders-სა და products-ს შორის)
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 1 CHECK (quantity > 0),
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT,
    CONSTRAINT unique_order_product UNIQUE (order_id, product_id)
);





-- testing with info





INSERT INTO customers (name, email) VALUES 
('Giorgi Maisuradze', 'giorgi.m@example.com'),
('Ana Kapanadze', 'ana.k@example.com'),
('Luka Shengelia', 'luka.sh@example.com');

INSERT INTO customer_profiles (customer_id, phone, address) VALUES 
(1, '+995-555-123-456', 'Tbilisi, Rustaveli Ave 12'),
(2, '+995-599-654-321', 'Batumi, Ninoshvili St 5'),
(3, '+995-577-111-222', 'Kutaisi, Tsereteli St 8');

INSERT INTO suppliers (name, contact_email) VALUES 
('Tech Hub Georgia', 'sales@techhub.ge'),
('Agro Import', 'info@agroimport.ge');

INSERT INTO products (name, price, supplier_id) VALUES 
('MacBook Pro 16', 7500.00, 1),
('Wireless Mouse', 120.50, 1),
('Mechanical Keyboard', 250.00, 1),
('Organic Coffee Beans', 45.00, 2),
('Green Tea', 18.50, 2);

INSERT INTO orders (customer_id, order_date) VALUES 
(1, '2026-08-15 10:30:00'),
(2, '2026-08-18 14:15:00'),
(1, '2026-08-20 09:00:00');

INSERT INTO order_items (order_id, product_id, quantity) VALUES 
(1, 1, 1), (1, 2, 1),
(2, 4, 3), (2, 5, 2),
(3, 3, 1);


SELECT * FROM customers
