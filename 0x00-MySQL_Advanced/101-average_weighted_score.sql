-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE done INT DEFAULT FALSE;
    DECLARE current_user_id INT;
    DECLARE sum_score FLOAT;
    DECLARE sum_weight FLOAT;
    DECLARE average_score FLOAT;

    -- Declare handler for no data found
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        -- Fetch next user id
        FETCH user_cursor INTO current_user_id;

        -- Break loop if no more users
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Calculate sum of weighted scores
        SELECT SUM(score * weight) INTO sum_score
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = current_user_id;

        -- Calculate sum of weights
        SELECT SUM(weight) INTO sum_weight
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = current_user_id;

        -- Calculate average weighted score
        SET average_score = sum_score / sum_weight;

        -- Update the average_score column for the user
        UPDATE users
        SET average_score = average_score
        WHERE id = current_user_id;
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;
END //
DELIMITER ;

