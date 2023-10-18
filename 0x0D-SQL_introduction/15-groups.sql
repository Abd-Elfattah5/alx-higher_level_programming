-- counting the same score records
SELECT score, COUNT(score) AS number FROM second_table ORDER BY score DESC GROUP BY score;
