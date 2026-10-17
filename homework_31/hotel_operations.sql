-- 1. ცხრილების შექმნა (CREATE TABLES)

CREATE TABLE hotels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    stars INT CHECK (stars BETWEEN 1 AND 5)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    hotel_id INT NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    floor INT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (hotel_id) REFERENCES hotels(id) ON DELETE CASCADE
);

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);

CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    room_id INT NOT NULL,
    service_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
);

-- 2. მონაცემების დამატება (INSERT DATA)

-- 2 სასტუმრო
INSERT INTO hotels (name, city, stars) VALUES
('Rooms Hotel', 'Tbilisi', 4),
('Radisson Blu', 'Batumi', 5);

-- 6 ნომერი (3-3 თითო სასტუმროში)
INSERT INTO rooms (hotel_id, room_number, floor, price_per_night) VALUES
(1, '101', 1, 250.00),
(1, '102', 1, 300.00),
(1, '201', 2, 450.00),
(2, '501', 5, 500.00),
(2, '502', 5, 550.00),
(2, '601', 6, 800.00);

-- 12 სტუმარი (2-2 თითო ნომერში)
INSERT INTO guests (room_id, first_name, last_name, phone_number) VALUES
(1, 'გიორგი', 'გიორგაძე', '599111111'),
(1, 'ანა', 'ბერიძე', '599222222'),
(2, 'დავით', 'კაპანაძე', '599333333'),
(2, 'მარიამ', 'ნოზაძე', '599444444'),
(3, 'ლუკა', 'ჩხეიძე', '599555555'),
(3, 'ნია', 'მაისურაძე', '599666666'),
(4, 'გიგა', 'კვარაცხელია', '599777777'),
(4, 'თამარ', 'ჯაფარიძე', '599888888'),
(5, 'ირაკლი', 'შენგელია', '599999999'),
(5, 'სალომე', 'მგელაძე', '599000000'),
(6, 'ზურაბ', 'აბაშიძე', '599123123'),
(6, 'ნათია', 'წიკლაური', '599321321');

-- სერვისები (მხოლოდ პირველ 5 ნომერს დავუმატეთ 2-2 სერვისი, რომ მე-6 ნომერი დარჩეს სერვისის გარეშე)
INSERT INTO services (room_id, service_name, price) VALUES
(1, 'Breakfast', 30.00),
(1, 'Spa', 50.00),
(2, 'Laundry', 20.00),
(2, 'Mini Bar', 45.00),
(3, 'Breakfast', 30.00),
(3, 'Airport Transfer', 70.00),
(4, 'Spa', 60.00),
(4, 'Room Cleaning', 15.00),
(5, 'Mini Bar', 80.00),
(5, 'Breakfast', 35.00);

-- -- 3. SQL მოთხოვნები (SELECT QUERIES)

-- -- ა) ყველა ნომერი შესაბამისი სასტუმროს სახელთან ერთად
-- SELECT r.room_number, r.floor, r.price_per_night, h.name AS hotel_name
-- FROM rooms r
-- JOIN hotels h ON r.hotel_id = h.id;

-- -- ბ) ყველა სტუმარი მისი ნომრის ნომრითა და სასტუმროს სახელით
-- SELECT g.first_name, g.last_name, r.room_number, h.name AS hotel_name
-- FROM guests g
-- JOIN rooms r ON g.room_id = r.id
-- JOIN hotels h ON r.hotel_id = h.id;

-- -- გ) კონკრეტული სასტუმროს (მაგ. 'Rooms Hotel') ყველა სტუმარი
-- SELECT g.first_name, g.last_name, h.name AS hotel_name
-- FROM guests g
-- JOIN rooms r ON g.room_id = r.id
-- JOIN hotels h ON r.hotel_id = h.id
-- WHERE h.name = 'Rooms Hotel';

-- -- დ) თითო სასტუმროში არსებული ნომრების რაოდენობა
-- SELECT h.name AS hotel_name, COUNT(r.id) AS room_count
-- FROM hotels h
-- LEFT JOIN rooms r ON h.id = r.hotel_id
-- GROUP BY h.id, h.name;

-- -- ე) ნომრები, რომელთათვისაც სერვისი ჯერ არ არის შეკვეთილი
-- SELECT r.id, r.room_number, h.name AS hotel_name
-- FROM rooms r
-- JOIN hotels h ON r.hotel_id = h.id
-- LEFT JOIN services s ON r.id = s.id AND s.room_id = r.id
-- WHERE s.id IS NULL;



--წაშლის ოპერაციები


-- 1.ერთი ნომრის (id = 1) წაშლა
-- DELETE FROM rooms 
-- WHERE id = 1;

-- /* 
--  დაკვირვება წაშლაზე:
--  ვინაიდან ცხრილების შექმნისას დავწერეთ 'FOREIGN KEY ... ON DELETE CASCADE',
--  ნომრის წაშლისთანავე მონაცემთა ბაზა ავტომატურად წაშლის იმ სტუმრებსა (guests)
--  და სერვისებს (services), რომლებიც მიბმულნი იყვნენ id = 1 ნომერზე.
-- */


-- -- 2.კონკრეტული ნომრის (id = 2) ღირებულების შეცვლა
-- UPDATE rooms 
-- SET price_per_night = 380.00 
-- WHERE id = 2;


-- 3. ერთი სტუმრის (id = 3) გადაწერა სხვა ნომერზე (room_id = 4)
-- UPDATE guests 
-- SET room_id = 4 
-- WHERE id = 3;