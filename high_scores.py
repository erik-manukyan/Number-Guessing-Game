import os
from datetime import datetime

def load_high_scores():
    """Load high scores from file, return empty list if file doesn't exist."""
    scores = []
    if os.path.exists("scores.txt"):
        try:
            with open("scores.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line and ":" in line:
                        parts = line.split(":")
                        if len(parts) >= 4:
                            date = parts[0]
                            difficulty = parts[1]
                            score = int(parts[2])
                            time_taken = float(parts[3])
                            scores.append({
                                "date": date,
                                "difficulty": difficulty,
                                "score": score,
                                "time": time_taken
                            })
        except (FileNotFoundError, ValueError, IndexError):
            # If file is corrupted or doesn't exist, start fresh
            scores = []
    return scores

def save_high_score(difficulty, score, time_taken):
    """Save a new high score to the file."""
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open("scores.txt", "a") as file:
        file.write(f"{date_str}:{difficulty}:{score}:{time_taken}\n")

def display_high_scores():
    """Display the top 10 high scores for each difficulty."""
    scores = load_high_scores()
    
    if not scores:
        print("No high scores yet! Be the first to set a record!")
        return
    
    # Separate scores by difficulty
    easy_scores = [s for s in scores if s["difficulty"] == "Easy"]
    medium_scores = [s for s in scores if s["difficulty"] == "Medium"]
    hard_scores = [s for s in scores if s["difficulty"] == "Hard"]
    
    # Sort by score (highest first)
    easy_scores.sort(key=lambda x: x["score"], reverse=True)
    medium_scores.sort(key=lambda x: x["score"], reverse=True)
    hard_scores.sort(key=lambda x: x["score"], reverse=True)
    
    print("\n" + "="*50)
    print("🏆 HIGH SCORES 🏆")
    print("="*50)
    
    # Display top scores for each difficulty
    difficulties = [("Easy", easy_scores), ("Medium", medium_scores), ("Hard", hard_scores)]
    
    for diff_name, diff_scores in difficulties:
        print(f"\n{diff_name} Mode:")
        print("-" * 20)
        if diff_scores:
            for i, score_data in enumerate(diff_scores[:5], 1):  # Top 5 for each difficulty
                print(f"{i}. {score_data['score']} pts - {score_data['time']}s - {score_data['date']}")
        else:
            print("No scores yet!")
    
    print("="*50)

def is_new_high_score(difficulty, score):
    """Check if the score qualifies as a high score (top 10 for difficulty)."""
    scores = load_high_scores()
    difficulty_scores = [s for s in scores if s["difficulty"] == difficulty]
    
    if len(difficulty_scores) < 10:
        return True
    
    difficulty_scores.sort(key=lambda x: x["score"], reverse=True)
    return score > difficulty_scores[9]["score"]  # Better than 10th place
