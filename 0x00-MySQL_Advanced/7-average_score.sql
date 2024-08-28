-- computes average
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE averagescore FLOAT;
DECLARE userid INT;
DECLARE counts INT;
DECLRE 
SET userid = user_id;
SELECT SUM(score), COUNT(user_id) INTO averagescore, counts
FROM corrections
WHERE user_id = userid;

UPDATE users
SET average_score = averagescore / counts
WHERE id = userid;
END $$
DELIMITER ;
