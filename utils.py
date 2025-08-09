import random

def random_bool(percentage_of_true):
    """Generate a random boolean based on given percentage of true outcomes."""
    probability_of_true = percentage_of_true / 100  # Convert percentage to probability
    return random.random() < probability_of_true

def intInputValid(message):
    """Get valid integer input from user with error handling."""
    while True:
        try:
            intInput = int(input(message))
            return intInput
        except ValueError:
            print("Please enter a valid number")

def getPlayerInput(message):
    """Get player input (either a number or 'H' for hint) with validation."""
    while True:
        user_input = input(message).strip().upper()
        if user_input == "H":
            return "H"
        try:
            number = int(user_input)
            return number
        except ValueError:
            print("Please enter a number or 'H' for hint")
