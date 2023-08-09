# GUESSING GAME

# THings we will need...
# 1. random number generation - X
# 2. guess tracker - X
# 3. user input - X
# 4. conditionals - did they win? - X
# 5. looping/iterating  - X
# 6. end of game - X
import random

def guess(start, stop):
    bad_guess = True

    while bad_guess:

        try:
            user_guess = int(input(f"Pick a number between {start} and {stop}: "))

        except ValueError:
            print("We need to input numbers, not letters")
            continue

        else: 
            if user_guess < start or user_guess > stop:
                print(f"Number needs to be between {start} and {stop}")
                continue

        bad_guess = False
    return user_guess    


def guessing_game():
    print("Welcome to the guessing game!")
    start = 1 
    stop = 20
    winning_number = random.randint(start, stop)
    guesses = 5

    while guesses > 0:
        # user_guess = int(input(f"Pick a number between {start} and {stop}: "))
        user_guess = guess(start, stop)
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed it! The number was {winning_number}! You used {5 - guesses} guesses!")
            # play again functionality
            return

        elif user_guess > winning_number:
            print(f"You guessed too high! Try again, you have {guesses} guesses left..")

        else:
            print(f"You guessed too low! Try again, you have {guesses} guesses left..")

    print(f"You are all out of guesses.  Sorry you lost.  The number was {winning_number}")

guessing_game()