import random
import time
from utils import intInputValid, getPlayerInput
from hints import provideHint
from scoring import calculateScore
from high_scores import save_high_score, display_high_scores, is_new_high_score

def welcome(): 
    """Function to display welcome message and handle difficulty selection."""
    print("""
        Welcome to the Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        You have 5 chances to guess the correct number.
        
        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        
        4. View High Scores
        5. Quit the Game""")
    
    # Get difficulty choice from user
    option = intInputValid("Enter your choice: ")
    while(option < 1 or option > 5):
        print("""Please choose a valid option
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)

        4. View High Scores
        5. Quit the Game""")
        option = intInputValid("Enter your choice: ")
    
    # Handle high scores option
    if option == 4:
        display_high_scores()
        input("\nPress Enter to continue...")
        return welcome()  # Show menu again
    
    # Exit if user chooses to quit
    if option == 5:
        return
    
    # Start game with selected difficulty
    gameLevel(option)

def gameLevel(option):
    """Function to handle different difficulty levels."""
    difficulty_names = {1: "Easy", 2: "Medium", 3: "Hard"}
    
    match option:
        case 1:  # Easy mode - 10 attempts
            print("Great! You have selected the Easy difficult level.")
            game(10, 100, "Easy")
        case 2:  # Medium mode - 5 attempts
            print("Great! You have selected the Medium difficult level.")
            game(5, 500, "Medium")
        case 3:  # Hard mode - 3 attempts
            print("Great! You have selected the Hard difficult level.")
            game(3, 1000, "Hard")

def game(guesses, points, difficulty):
    """Main game function that handles the guessing logic."""
    # Initialize game variables
    storeGuess = []  # Store all player guesses for hint comparisons
    usedHints = []  # Track hints used in this game session
    overall_point_lost = 0  # Track total hint penalties
    
    guessNum = random.randint(1, 100)  # Generate random secret number
    print("Let's start the game!")
    print("(Enter a number to guess, or 'H' to get a hint)")
    
    # Start timing the game
    start_time = time.time()
    
    playerNum = -1  # Initialize player's guess
    counter = 0  # Count number of attempts used
    
    # Main game loop - continue until correct guess or out of attempts
    while (guessNum != playerNum and counter != guesses):
        user_input = getPlayerInput("Enter your guess (or 'H' for hint): ")
        
        # Handle hint request
        if user_input == "H":
            points_lost = provideHint(guessNum, storeGuess, guesses, usedHints)
            if points_lost:  # Check if hint was actually given
                print(f"Points deducted: {points_lost}")
                overall_point_lost += points_lost
            continue  # Don't count hint request as a guess
            
        # Handle number guess
        playerNum = user_input  # It's a number
        if (guessNum > playerNum):
            print("Incorrect! The number is more than %s" %playerNum)
            counter += 1
            storeGuess.append(playerNum)
        elif (guessNum < playerNum):
            print("Incorrect! The number is less than %s" %playerNum)
            counter += 1
            storeGuess.append(playerNum)
        else:
            # Correct guess - player wins!
            storeGuess.append(playerNum)
            counter += 1
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            final_score = calculateScore(counter, guesses, elapsed_time, overall_point_lost)
            print("Congratulations! You guessed the number in %s attempts" %counter)
            print("Time taken: %s seconds" %elapsed_time)
            print(f"Your final score: {final_score} points!")
            
            # Check and save high score
            if is_new_high_score(difficulty, final_score):
                print("🎉 NEW HIGH SCORE! 🎉")
                save_high_score(difficulty, final_score, elapsed_time)
            else:
                print("Good job! Try to beat the high scores!")
            
            print()
            break
        
    # Game over - player ran out of attempts
    if counter == guesses:
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)
        final_score = calculateScore(counter, guesses, elapsed_time, overall_point_lost)
        print("""
        GAME OVER!")
        No chances left
        The number was:""", guessNum)
        print("Time taken: %s seconds" %elapsed_time)
        print(f"Your final score: {final_score} points!")
        
        # Check and save high score even on loss
        if is_new_high_score(difficulty, final_score):
            print("🎉 NEW HIGH SCORE! 🎉")
            save_high_score(difficulty, final_score, elapsed_time)
        else:
            print("Try again to beat the high scores!")

def main():
    """Main function to run the game with continue/quit option."""
    while True:
        # Start a new game round
        welcome()
        
        # Ask if player wants to continue playing
        cont = input("Would you like to continue to play? Y/N: ").lower()
        while (cont != "y" and cont != "n"):
            print("Please enter Y or N")
            cont = input("Would you like to continue to play? Y/N: ").lower()
        
        # Exit if player chooses not to continue
        if cont == "n":
            print("Thanks for playing!")
            break
