-- Prints state and max trmperature ordered
-- by temperature in descendijg order for the data
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY max_temp DESC;
