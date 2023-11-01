# GUESSING GAME

# Things we will need...
# 1. random - generate random numbers 
# 2. user input 
# 3. iterating 
# 4. guess tracker - number of guesses 
# 5. conditionals
# 6. helper function maybe?
from random import randint


def guess(start, end):
    bad_guess = True

    while bad_guess:
        try:
            user_guess = int(input(f"Pick a number from {start} to {end}: "))

        except ValueError:
            print("We need to enter numbers only for the guessing game!")
            continue

        else:
            if user_guess < start or user_guess > end:
                print(f"Numbers need to be between {start} and {end}, not {user_guess}")
                continue

        bad_guess = False
    return user_guess

     

def guessing_game():
    """guessing game function!"""
    print("Welcome to the guessing game!")
    start = 1
    end = 20
    winning_num = randint(start, end)
    guesses = 5

    while guesses > 0:
        # user_guess = int(input(f"Pick a number from {start} to {end}: "))
        user_guess = guess(start, end)
        guesses -= 1

        if user_guess == winning_num:
            print(f"You guessed it!!! The number was {winning_num}! You used {5 - guesses} guesses to win!  Yay!")
            # play again functionality
            return

        elif user_guess > winning_num:
            print(f"You guessed too high!  Try again! You have {guesses} guesses left!")
            continue

        else:
            print(f"You guessed too low!  Try again! You have {guesses} guesses left!")
            continue

    print(f"You ran out of guesses, sorry you lost.  The winning number was {winning_num}")


   
guessing_game()