-- Print number of scores for the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;;
