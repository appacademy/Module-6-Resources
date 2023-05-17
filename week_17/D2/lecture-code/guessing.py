# Guessing Game 
# User guesses a random number until they guess 
# it or run out of tries 

# Game Plan
# 1. user input - x
# 2. random number - x
# 3. loop/iterate - x
# 4. limit to a number of guesses - x
# 5. conditaionsl check if the use won/lost
from random import randint


def guess(start, end):
    bad_guess = True

    while bad_guess:
        try:
            user_guess = int(input(f"Pick a number from {start} to {end}: "))
        
        except ValueError:
            print("We need to enter numbers not strings to play the game")
            continue

        else:
            if user_guess < start or user_guess > end:
                print(f"Numbers need to be in the range of {start} and {end}, you picked {user_guess}")
                continue


        bad_guess = False

    return user_guess


def guessing_game():
    print("Welcome to the guessing game!")
    guesses = 5
    start = 1
    end = 20
    winning_number = randint(start, end)

    while guesses > 0:
        # user_guess = int(input(f"Pick a number from {start} to {end}: "))
        user_guess = guess(start, end)
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed correctly!  The number was {winning_number}")
            return
        
        elif user_guess > winning_number:
            print(f"You guessed to high!  Try again!  You have {guesses} guesses left!")

        else:
            print(f"You guessed to low!  Try again!  You have {guesses} guesses left!")

    print(f"You are out of guesses.  Game over! The number was {winning_number}")


guessing_game()