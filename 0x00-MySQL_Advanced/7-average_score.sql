-- a SQL script that creates a stored procedure ComputerAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SET @av = (SELECT AVG(score) AS av FROM corrections WHERE user_id=user_id);
	UPDATE users SET average_score= @av where id = user_id;
END //
DELIMITER;
