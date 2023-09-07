# GUESSING GAME

# Things we will need...
# 1. random number X
# 2. looping / iterating X
# 3. user input X
# 4. conditionals X
# 5. feedback X
# 6. validate our input x
import random

def guess(start, end):
    bad_guess = True

    while bad_guess:
        try:
            user_input = int(input(f"Pick a number from {start} to {end}: "))

        except ValueError:
            print('We need to enter numbers for the guessing game, not letters!')
            continue

        else: 
            if user_input < start or user_input > end:
                print(f"Numbers need to be between {start} and {end}, not {user_input}")
                continue
        
        bad_guess = False

    return user_input

def guessing_game():
    print('Welcome to the guessing game!')
    start = 1
    end = 50
    guesses = 5
    winning_number = random.randint(start, end)


    while guesses > 0:
        # user_guess = int(input(f"Pick a number from {start} to {end}: "))
        # play_again = input('Do you want to play again, enter "Y" for yes or "N" for no').upper()
        # if play_again == "Y":
        #     guessing_game()
        user_guess = guess(start, end)
        guesses -= 1

        if user_guess == winning_number:
            print(f"You guessed it!  The number was {winning_number}! You used {5 - guesses} guesses!")
            # implement play again?
            return 

        elif user_guess > winning_number:
            print(f"You guessed too high!  Try again!  You have {guesses} guesses left")

        else:
            print(f"You guessed too low!  Try again!  You have {guesses} guesses left")
    
    print(f"You ran out of guesses. Sorry you lost, the number was {winning_number}")


guessing_game()