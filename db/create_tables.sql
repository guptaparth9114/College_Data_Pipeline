DROP TABLE IF EXISTS colleges;

CREATE TABLE colleges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    state VARCHAR(100),
    ug_fee INT,
    pg_fee INT,
    rating FLOAT,
    academic FLOAT,
    accommodation FLOAT,
    faculty FLOAT,
    infrastructure FLOAT,
    placement FLOAT,
    social_life FLOAT
);
