import random
import math
from utils import random_bool

def fibonacci_until(max_num):
    """Helper function to create a fibonacci sequence up to max_num."""
    sequence = []
    a, b = 0, 1
    while a <= max_num:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def isPrime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPerfectSquare(n):
    """Helper function to check if a number is a perfect square."""
    root = int(math.sqrt(n))
    return root * root == n

def provideHint(guessNum, storeGuess, guesses, usedHints=None):
    """Function to provide random hints about the secret number."""
    # Initialize usedHints list if not provided
    if usedHints is None:
        usedHints = []

    # Get list of hint types that haven't been used yet
    available_hints = [i for i in range(11) if i not in usedHints]

    # If all hints have been used, inform player
    if not available_hints:
        print("Sorry no hints left")
        return

    # Select a random unused hint type
    randInt = random.choice(available_hints)
    usedHints.append(randInt)
    
    match randInt:
        case 0:  # Even/Odd hint
            if guessNum % 2 == 0:
                print("The number is even")
            else:
                print("The number is odd")
            pointsDeducted = 50
        case 1:  # Divisible by number hint
            listOfDivisors = list(range(3, 101))
            for numbers in listOfDivisors:
                if isPrime(numbers):
                    listOfDivisors.remove(numbers)
            if isPrime(guessNum) == False: 
                for i in listOfDivisors:
                    if guessNum % i == 0:
                        print("The number is divisible by", i)
                        pointsDeducted = 30
                        break
            else:
                listOfRandomNumbers = []
                if guesses == 10:
                    if random_bool(50):
                        listOfRandomNumbers.append(guessNum)
                    else:
                        listOfRandomNumbers.append(random.randint(1, 100))
                elif guesses == 5:
                    if random_bool(25):
                        listOfRandomNumbers.append(guessNum)
                    else:
                        listOfRandomNumbers.append(random.randint(1, 100))
                else:
                    if random_bool(10):
                        listOfRandomNumbers.append(guessNum)
                    else:
                        listOfRandomNumbers.append(random.randint(1, 100))

                for i in range(1, 20):
                    while True:  # Keep generating until we get a unique number
                        newNum = random.randint(1, 100)
                        if newNum not in listOfRandomNumbers:
                            listOfRandomNumbers.append(newNum)
                            break  # Exit the while loop once we add a unique number

                
                for i in listOfRandomNumbers:
                    print(i, end=",")
                print("The number might be here")

                pointsDeducted = 30
        case 2:  # Fibonacci hint
            fibonacciSequence = fibonacci_until(guessNum + 1)
            if guessNum in fibonacciSequence:
                print("The number is in a fibonacci sequence")
            else:
                print("The number is not a fibonacci sequence")
            pointsDeducted = 10  # Hard hint
        case 3:  # Multiple of digit sum hint
            if guessNum > 9:
                numString = str(guessNum)
                digit1 = int(numString[0])  # Fixed: was guessNum[0]
                digit2 = int(numString[1])  # Fixed: was guessNum[1]
                if guessNum % (digit1 + digit2) == 0:
                    print("The number is a multiple of the sum of its digits")
                else:
                    print("The number is not a multiple of the sum of its digits")
            else:
                numString = str(guessNum)
                print("The number ends on", numString[-1])
            pointsDeducted = 10  # Hard hint
        case 4:  # Greater/Less than 50 hint
            if guessNum > 50:
                print("The number is bigger than 50")
            else:
                print("The number is smaller then 50")
            pointsDeducted = 50  # Easy hint
        case 5:  # Quarter range hint
            if guessNum <= 25:
                print("The number is in the first quarter")
            elif guessNum > 25 and guessNum < 50:
                print("The number is in the second quarter")
            elif guessNum >= 50 and guessNum <= 75:
                print("The number is in the third quarter")
            else:
                print("The number is in the fourth quarter")
            pointsDeducted = 50  # Easy hint
        case 6:  # Number of digits hint
            if guessNum < 10:
                print("The number has 1 digit")
            else:
                print("The number has 2 digits")
            pointsDeducted = 50  # Easy hint
        case 7:  # Sum of digits hint
            if guessNum > 9:
                numString = str(guessNum)
                digit1 = int(numString[0])
                digit2 = int(numString[1])
                if digit1 + digit2 > 10:
                    print("The sum of digits is greater than 10")
                else:
                    print("The sum of digits is smaller than 10")
            else:
                print("The number has 1 digit")
            pointsDeducted = 30  # Medium hint
        case 8:  # Prime/Perfect square hint
            if isPrime(guessNum):
                print("The number is prime")
                pointsDeducted = 10  # Hard hint
                return pointsDeducted
            elif isPerfectSquare(guessNum):
                print("The number is a perfect square")
                pointsDeducted = 10  # Hard hint
                return pointsDeducted
            else:
                # If neither prime nor perfect square, call another hint
                return provideHint(guessNum, storeGuess, guesses, usedHints)
        case 9:  # Comparison with previous guess hint
            if storeGuess:
                if guessNum > storeGuess[-1]:
                    bigger = True
                else:
                    bigger = False
                
                if bigger:
                    difference = guessNum - storeGuess[-1]
                else:
                    difference = storeGuess[-1] - guessNum
                
                if difference > 50:
                    print("The number is greater than your last guess by more than 50")
                elif difference > 25:
                    print("The number is greater than your last guess by more than 25")
                else:
                    print("The number is close to being discovered!")
                pointsDeducted = 10  # Hard hint
            else:
                # If no previous guesses, call another hint
                return provideHint(guessNum, storeGuess, guesses, usedHints)
                
        case 10:  # Repeated digits hint
            if guessNum > 9:
                numString = str(guessNum)
                digit1 = int(numString[0])
                digit2 = int(numString[1])
                if digit1 == digit2:
                    print("The number has repeated digits")
                else:
                    print("The number does not have repeated digits")
            else:
                print("The number does not have repeated digits")
            pointsDeducted = 30  # Medium hint
    
    return pointsDeducted
