def calculateScore(attempts_used, max_attempts, time_taken, hint_penalties):
    """Calculate the final score based on attempts, time, and penalties."""
    match max_attempts:
        case 10:
            base_points = 100
            unused_points = 10
            perfect_game = 50
            time_points = 60
            perfect_time = 30
        case 5:
            base_points = 500
            unused_points = 50
            perfect_game = 150
            time_points = 300
            perfect_time = 150
            hint_penalties *= 5
        case 3:
            base_points = 1000
            unused_points = 100
            perfect_game = 300
            time_points = 600
            perfect_time = 300
            hint_penalties *= 5
    
    if attempts_used == 1:
        was_perfect_game = True
    else:
        was_perfect_game = False

    # Main Calculation

    attempt_bonus = unused_points * (max_attempts - attempts_used)
    
    # Calculate time bonus using linear scaling
    if time_taken <= 10:
        time_bonus = time_points + perfect_time  # Full bonus + perfect time bonus for 10 seconds or less
    elif time_taken <= 60:  # Use 60 seconds as cutoff for time bonus
        # Linear scaling: bonus decreases from time_points to 0
        time_bonus = time_points * (60 - time_taken) / (60 - 10)
    else:
        time_bonus = 0  # No bonus for times longer than 60 seconds
    
    # Round time bonus to avoid decimal points in score
    time_bonus = round(time_bonus)

    final_score = base_points + attempt_bonus + time_bonus
    if was_perfect_game:
        final_score += perfect_game
    
    # Subtract hint penalties
    final_score -= hint_penalties

    return final_score
