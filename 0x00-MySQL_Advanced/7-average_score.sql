-- computes average
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE averagescore FLOAT;
DECLARE userid INT ;
DECLARE counts INT;
DECLARE totalsum INT;

SELECT SUM(score) INTO totalsum
FROM corrections
WHERE corrections.user_id = user_id;

SELECT COUNT(user_id) INTO counts
FROM corrections
WHERE corrections.user_id = user_id;

SET averagescore = totalsum / counts;
IF counts > 0 THEN
	UPDATE users
	SET average_score = averagescore
	WHERE users.id = user_id;
ELSE 
	UPDATE users
	SET average_score = 0
	WHERE users.id = user_id;
END IF;
END $$
DELIMITER ;
