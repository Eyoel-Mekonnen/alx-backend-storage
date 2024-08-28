-- computes average
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE averagescore FLOAT;
DECLARE userid INT;
DECLARE counts INT;
SET userid = user_id;
SELECT SUM(score), COUNT(user_id) INTO averagescore, counts
FROM corrections
WHERE user_id = userid;
IF counts > 0 THEN
	UPDATE users
	SET average_score = averagescore / counts
	WHERE id = userid;
ELSE 
	UPDATE users
	SET average_score = 0
	WHERE id = userid;
END IF;
END $$
DELIMITER ;
