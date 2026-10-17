CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    release_year INT NOT NULL CHECK (release_year >= 1886),
    vin VARCHAR(17) UNIQUE CHECK (LENGTH(vin) <= 17),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    engine_capacity NUMERIC(3, 1) CHECK (engine_capacity > 0.5),
    mileage INT CHECK (mileage >= 0),
    is_cleared BOOLEAN NOT NULL DEFAULT FALSE,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    description TEXT,
    is_sold BOOLEAN NOT NULL DEFAULT FALSE
);

INSERT INTO cars (brand, model, release_year, vin, engine_capacity, mileage, is_cleared, price, description, is_sold) 
VALUES
('BMW', 'M5 CS', 2022, 'WBS83CH00N1234567', 4.4, 15000, TRUE, 125000.00, 'Ideal condition, full spec.', FALSE),
('Toyota', 'Camry', 2020, '4T1C11AK0LU123456', 2.5, 65000, TRUE, 22000.00, 'Reliable daily driver.', FALSE),
('Mercedes-Benz', 'E 300', 2021, 'W1K2183111A123456', 2.0, 42000, TRUE, 45000.00, 'AMG exterior package.', TRUE),
('Porsche', '911 GT3', 2023, 'WP0AD2A91NS123456', 4.0, 3200, TRUE, 210000.00, 'Track package, flawless.', FALSE),
('Ford', 'Mustang GT', 2018, '1FA6P8CF0J5123456', 5.0, 85000, FALSE, 28500.50, 'Low mileage, minor repairs needed.', FALSE),
('Audi', 'RS6 Avant', 2022, 'WAUZZZF21NN123456', 4.0, 21000, TRUE, 115000.00, 'Full factory warranty.', FALSE),
('Honda', 'Civic', 2019, '1HGFC2F60KH123456', 1.5, 92000, TRUE, 16800.00, 'Great fuel economy.', TRUE),
('Subaru', 'WRX STI', 2017, 'JF1VA2E68H9123456', 2.5, 110000, FALSE, 21000.00, 'Aftermarket exhaust installed.', FALSE),
('Tesla', 'Model S', 2021, '5YJSA1E21MF123456', 1.0, 35000, TRUE, 68000.00, 'Dual Motor, Autopilot package.', FALSE),
('BMW', 'X5 M', 2020, '5UX53DP02L9123456', 4.4, 58000, TRUE, 72000.00, 'Panoramic roof, M-Performance details.', FALSE);




-- SELECT * FROM cars;
-- SELECT brand, model, release_year, price FROM cars;
-- SELECT * FROM cars WHERE brand = 'Mercedes-benz';


-- romelic gvinda imas komentaris nishani movushalot