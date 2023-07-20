-- Create table unique_id with default id of 1
-- and id must always be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
