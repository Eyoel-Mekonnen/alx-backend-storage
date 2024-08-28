-- create a procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE projectid INT;
	SELECT id INTO projectid FROM projects WHERE name = project_name;
	IF projectid IS NOT NULL THEN
		INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, projectid, score);
	ELSE
		INSERT INTO projects(name) VALUES (project_name);
		SELECT id INTO projectid FROM projects WHERE name = project_name;
		INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, projectid, score);
	END IF;
END $$
DELIMITER ;
