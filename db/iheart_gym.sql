DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS gymclasses;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob DATE,
    membership VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE gymclasses (
    id SERIAL PRIMARY KEY,
    gymclass_name VARCHAR(255),
    instructor VARCHAR(255),
    date DATE,
    start_time TIME,
    duration INT,
    capacity INT,
    active boolean
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id SERIAL REFERENCES members(id) ON DELETE CASCADE,
    gymclass_id SERIAL REFERENCES gymclasses(id) ON DELETE CASCADE
);