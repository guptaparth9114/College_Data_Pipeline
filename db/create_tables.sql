CREATE TABLE colleges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    state VARCHAR(100),
    city VARCHAR(100),
    ranking INT,
    tuition_fee INT,
    placement_rate FLOAT,
    program_offered VARCHAR(255)
);
