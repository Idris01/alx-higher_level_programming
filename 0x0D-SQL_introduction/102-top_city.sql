-- Prints top 3 cities with highest average 
-- temperature  in month of July and Augustordered
-- by temperature in descendijg order for the data
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
