-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE sum_score FLOAT;
    DECLARE sum_weight FLOAT;
    DECLARE average_score FLOAT;

    -- Calculate sum of weighted scores
    SELECT SUM(score * weight) INTO sum_score
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate sum of weights
    SELECT SUM(weight) INTO sum_weight
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate average weighted score
    SET average_score = sum_score / sum_weight;

    -- Update the average_score column for the user
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //
DELIMITER ;
