-- ============================================================
--  CineVerse - Complete Database Setup Script (All-in-One)
-- ============================================================

-- 1️⃣ CREATE DATABASE
CREATE DATABASE IF NOT EXISTS movie_db
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_general_ci;

USE movie_db;

-- ============================================================
-- 2️⃣ CREATE TABLES
-- ============================================================

CREATE TABLE IF NOT EXISTS movie (
  movie_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  genre VARCHAR(100),
  duration VARCHAR(20),
  release_date DATE,
  UNIQUE KEY uq_movie_title (title(200))
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS showtime (
  show_id INT AUTO_INCREMENT PRIMARY KEY,
  movie_id INT NOT NULL,
  show_date DATE NOT NULL,
  show_time TIME NOT NULL,
  total_seats INT NOT NULL DEFAULT 100,
  available_seats INT NOT NULL DEFAULT 100,
  FOREIGN KEY (movie_id) REFERENCES movie(movie_id) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS booking (
  booking_id INT AUTO_INCREMENT PRIMARY KEY,
  show_id INT NOT NULL,
  customer_name VARCHAR(150) NOT NULL,
  seats_booked INT NOT NULL CHECK (seats_booked > 0),
  booking_date DATE NOT NULL,
  FOREIGN KEY (show_id) REFERENCES showtime(show_id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ============================================================
-- 3️⃣ INSERT 100 MOVIES
-- ============================================================

INSERT INTO movie (title, genre, duration, release_date) VALUES
('Inception', 'Sci-Fi', '2h28m', '2010-07-16'),
('Interstellar', 'Sci-Fi', '2h49m', '2014-11-07'),
('The Dark Knight', 'Action', '2h32m', '2008-07-18'),
('Avengers: Endgame', 'Action', '3h01m', '2019-04-26'),
('Titanic', 'Romance', '3h14m', '1997-12-19'),
('Avatar', 'Fantasy', '2h42m', '2009-12-18'),
('The Lion King', 'Animation', '1h28m', '1994-06-24'),
('Frozen', 'Animation', '1h42m', '2013-11-27'),
('Toy Story', 'Animation', '1h21m', '1995-11-22'),
('Finding Nemo', 'Animation', '1h40m', '2003-05-30'),
('Gladiator', 'Action', '2h35m', '2000-05-05'),
('Joker', 'Thriller', '2h02m', '2019-10-04'),
('The Shawshank Redemption', 'Drama', '2h22m', '1994-09-23'),
('Forrest Gump', 'Drama', '2h24m', '1994-07-06'),
('The Matrix', 'Sci-Fi', '2h16m', '1999-03-31'),
('The Godfather', 'Crime', '2h55m', '1972-03-24'),
('The Godfather Part II', 'Crime', '3h22m', '1974-12-20'),
('The Batman', 'Action', '2h56m', '2022-03-04'),
('Iron Man', 'Action', '2h06m', '2008-05-02'),
('Doctor Strange', 'Fantasy', '1h55m', '2016-11-04'),
('Spider-Man: No Way Home', 'Action', '2h28m', '2021-12-17'),
('Black Panther', 'Action', '2h14m', '2018-02-16'),
('Captain America: Civil War', 'Action', '2h27m', '2016-05-06'),
('Avengers: Infinity War', 'Action', '2h29m', '2018-04-27'),
('Guardians of the Galaxy', 'Sci-Fi', '2h01m', '2014-08-01'),
('Ant-Man', 'Action', '1h57m', '2015-07-17'),
('Thor: Ragnarok', 'Action', '2h10m', '2017-11-03'),
('Doctor Strange in the Multiverse of Madness', 'Fantasy', '2h06m', '2022-05-06'),
('The Avengers', 'Action', '2h23m', '2012-05-04'),
('Captain Marvel', 'Action', '2h03m', '2019-03-08'),
('Black Widow', 'Action', '2h14m', '2021-07-09'),
('Shang-Chi and the Legend of the Ten Rings', 'Action', '2h12m', '2021-09-03'),
('Eternals', 'Action', '2h36m', '2021-11-05'),
('The Flash', 'Action', '2h24m', '2023-06-16'),
('The Suicide Squad', 'Action', '2h12m', '2021-08-06'),
('Wonder Woman', 'Action', '2h21m', '2017-06-02'),
('Aquaman', 'Action', '2h23m', '2018-12-21'),
('Justice League', 'Action', '2h00m', '2017-11-17'),
('Man of Steel', 'Action', '2h23m', '2013-06-14'),
('Batman v Superman: Dawn of Justice', 'Action', '2h31m', '2016-03-25'),
('Deadpool', 'Comedy', '1h48m', '2016-02-12'),
('Deadpool 2', 'Comedy', '1h59m', '2018-05-18'),
('Logan', 'Action', '2h17m', '2017-03-03'),
('X-Men: Days of Future Past', 'Action', '2h12m', '2014-05-23'),
('The Wolverine', 'Action', '2h06m', '2013-07-26'),
('Venom', 'Action', '1h52m', '2018-10-05'),
('Venom: Let There Be Carnage', 'Action', '1h37m', '2021-10-01'),
('Morbius', 'Action', '1h44m', '2022-04-01'),
('Guardians of the Galaxy Vol. 3', 'Action', '2h30m', '2023-05-05'),
('Dune', 'Sci-Fi', '2h35m', '2021-10-22'),
('Tenet', 'Sci-Fi', '2h30m', '2020-08-26'),
('Oppenheimer', 'Biography', '3h00m', '2023-07-21'),
('Barbie', 'Comedy', '1h54m', '2023-07-21'),
('Mission: Impossible - Fallout', 'Action', '2h27m', '2018-07-27'),
('Mission: Impossible - Dead Reckoning', 'Action', '2h44m', '2023-07-12'),
('Top Gun: Maverick', 'Action', '2h11m', '2022-05-27'),
('Fast & Furious 7', 'Action', '2h17m', '2015-04-03'),
('Fast & Furious 9', 'Action', '2h23m', '2021-06-25'),
('Transformers', 'Action', '2h24m', '2007-07-03'),
('Transformers: Rise of the Beasts', 'Action', '2h07m', '2023-06-09'),
('John Wick', 'Action', '1h41m', '2014-10-24'),
('John Wick: Chapter 2', 'Action', '2h02m', '2017-02-10'),
('John Wick: Chapter 3', 'Action', '2h11m', '2019-05-17'),
('John Wick: Chapter 4', 'Action', '2h49m', '2023-03-24'),
('It', 'Horror', '2h15m', '2017-09-08'),
('It Chapter Two', 'Horror', '2h49m', '2019-09-06'),
('The Conjuring', 'Horror', '1h52m', '2013-07-19'),
('The Conjuring 2', 'Horror', '2h14m', '2016-06-10'),
('Annabelle', 'Horror', '1h39m', '2014-10-03'),
('The Nun', 'Horror', '1h36m', '2018-09-07'),
('The Nun II', 'Horror', '1h50m', '2023-09-08'),
('Insidious', 'Horror', '1h43m', '2010-04-01'),
('Insidious: The Red Door', 'Horror', '1h47m', '2023-07-07'),
('Frozen II', 'Animation', '1h43m', '2019-11-22'),
('Moana', 'Animation', '1h47m', '2016-11-23'),
('Zootopia', 'Animation', '1h48m', '2016-03-04'),
('Encanto', 'Animation', '1h42m', '2021-11-24'),
('Coco', 'Animation', '1h45m', '2017-11-22'),
('Inside Out', 'Animation', '1h35m', '2015-06-19'),
('The Incredibles', 'Animation', '1h55m', '2004-11-05'),
('The Incredibles 2', 'Animation', '1h58m', '2018-06-15'),
('Ratatouille', 'Animation', '1h51m', '2007-06-29'),
('Up', 'Animation', '1h36m', '2009-05-29'),
('WALL-E', 'Animation', '1h38m', '2008-06-27'),
('Brave', 'Animation', '1h33m', '2012-06-22'),
('Big Hero 6', 'Animation', '1h48m', '2014-11-07'),
('Monsters, Inc.', 'Animation', '1h32m', '2001-11-02'),
('Monsters University', 'Animation', '1h44m', '2013-06-21'),
('The Good Dinosaur', 'Animation', '1h33m', '2015-11-25'),
('Finding Dory', 'Animation', '1h37m', '2016-06-17'),
('Lightyear', 'Animation', '1h45m', '2022-06-17'),
('Turning Red', 'Animation', '1h40m', '2022-03-11'),
('Soul', 'Animation', '1h40m', '2020-12-25'),
('Luca', 'Animation', '1h35m', '2021-06-18'),
('Elemental', 'Animation', '1h42m', '2023-06-16'),
('Wish', 'Animation', '1h35m', '2023-11-22');

-- ============================================================
-- 4️⃣ INSERT SAMPLE SHOWTIMES
-- ============================================================

INSERT INTO showtime (movie_id, show_date, show_time, total_seats, available_seats)
VALUES
  ((SELECT movie_id FROM movie WHERE title='Inception' LIMIT 1), '2025-12-01', '18:00:00', 100, 100),
  ((SELECT movie_id FROM movie WHERE title='Interstellar' LIMIT 1), '2025-12-01', '20:30:00', 80, 80),
  ((SELECT movie_id FROM movie WHERE title='The Dark Knight' LIMIT 1), '2025-12-01', '19:00:00', 120, 120),
  ((SELECT movie_id FROM movie WHERE title='Avengers: Endgame' LIMIT 1), '2025-12-02', '18:30:00', 150, 150),
  ((SELECT movie_id FROM movie WHERE title='Titanic' LIMIT 1), '2025-12-02', '17:00:00', 100, 100),
  ((SELECT movie_id FROM movie WHERE title='Iron Man' LIMIT 1), '2025-12-03', '19:30:00', 90, 90),
  ((SELECT movie_id FROM movie WHERE title='Spider-Man: No Way Home' LIMIT 1), '2025-12-03', '21:00:00', 90, 90),
  ((SELECT movie_id FROM movie WHERE title='Frozen' LIMIT 1), '2025-12-04', '10:00:00', 80, 80),
  ((SELECT movie_id FROM movie WHERE title='Finding Nemo' LIMIT 1), '2025-12-04', '11:30:00', 80, 80),
  ((SELECT movie_id FROM movie WHERE title='Dune' LIMIT 1), '2025-12-05', '20:00:00', 100, 100);

-- ============================================================
-- 5️⃣ INSERT SAMPLE BOOKINGS
-- ============================================================

INSERT INTO booking (show_id, customer_name, seats_booked, booking_date)
VALUES
  ((SELECT show_id FROM showtime WHERE movie_id=(SELECT movie_id FROM movie WHERE title='Inception') LIMIT 1), 'Aman Tiwari', 3, '2025-11-20'),
  ((SELECT show_id FROM showtime WHERE movie_id=(SELECT movie_id FROM movie WHERE title='Interstellar') LIMIT 1), 'Riya Sharma', 2, '2025-11-21'),
  ((SELECT show_id FROM showtime WHERE movie_id=(SELECT movie_id FROM movie WHERE title='The Dark Knight') LIMIT 1), 'Rahul Verma', 4, '2025-11-22');

-- ============================================================
-- 6️⃣ USEFUL TEST QUERIES
-- ============================================================

-- Total movies
SELECT COUNT(*) AS total_movies FROM movie;

-- View full booking details
SELECT b.booking_id, b.customer_name, m.title, b.seats_booked, b.booking_date
FROM booking b
JOIN showtime s ON b.show_id = s.show_id
JOIN movie m ON s.movie_id = m.movie_id
ORDER BY b.booking_date DESC;

-- Showtimes for Inception
SELECT s.show_id, m.title, s.show_date, s.show_time, s.available_seats
FROM showtime s
JOIN movie m ON s.movie_id = m.movie_id
WHERE m.title = 'Inception';

-- Booking count per movie
SELECT m.title, COUNT(b.booking_id) AS bookings_count
FROM booking b
JOIN showtime s ON b.show_id = s.show_id
JOIN movie m ON s.movie_id = m.movie_id
GROUP BY m.title
ORDER BY bookings_count DESC;

-- ============================================================
-- 7️⃣ OPTIONAL TRIGGER - AUTO DECREMENT SEATS
-- ============================================================

-- Deliberately optional — enable only if you want automatic seat deduction.
-- If enabled, ensure your app checks seat availability first.

-- DELIMITER //
-- CREATE TRIGGER trg_after_booking_insert
-- AFTER INSERT ON booking
-- FOR EACH ROW
-- BEGIN
--   UPDATE showtime
--   SET available_seats = GREATEST(0, available_seats - NEW.seats_booked)
--   WHERE show_id = NEW.show_id;
-- END;
-- //
-- DELIMITER ;

-- ============================================================
-- END OF SCRIPT
-- ============================================================
