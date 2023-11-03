# SNOWMAN CODE GOES HERE!
from random import choice
from stages import snowman
from logo import logo
import os


# def get_game_word():
#     """reads in a game word from our file"""
#     # f = open("words.txt", "r")
#     # words = [word.rstrip() for word in f]
#     # words = open("words.txt", "r").read().split()
#     # print(words)
#     return choice(open("words.txt", "r").read().split())


def printer(snowman, chances, guesses, display, error=None):
            if error:
                print(error)
            print(snowman[chances])
            print(" ".join(display))
            print(f"You have guessed: {guesses}")



def play_snowman():
    os.system("clear")
    print(logo)
    print("Welcome to ⛄️⛄️⛄️ Snowman! ⛄️⛄️⛄️")
    print("♫♬ DO YOU WANT TO MELT A SNOWMAN!!! ♫♬")
    print("Guess the word before frosty melts... 💧")    
    game_word = choice(open("words.txt", "r").read().split())
    display = ["_" for _ in range(len(game_word))]
    chances = 0
    guesses = set()
    print(snowman[chances])
    print(" ".join(display))


    play = True
    while play:
        guess = input('Guess a letter: ').lower()
        os.system("clear")

        if guess in guesses:
            error = f"You already guessed {guess.upper()}, try again!"
            printer(snowman, chances, guesses, display, error)
            continue

        if guess not in "abcdefghijklmnopqrstuvwxyz":
            error = "You can only guess letters, try again, no penalty"
            printer(snowman, chances, guesses, display, error)
            continue

        guesses.add(guess)

        for index, letter in enumerate(game_word):
            if letter == guess:
                display[index] = letter.upper()

        if guess not in game_word:
            chances += 1
            print(f'Sorry, "{guess.upper()}" is not in the game word...')
            if chances == 6:
                os.system("clear")
                print(snowman[-1])
                play = False
                print(f"YOU LOSE: The word was {game_word.upper()}.  POOR FROSTY...💧💧💧")
                return

        printer(snowman, chances, guesses, display)

        if '_' not in display:
            play = False
            print(f"{game_word.upper()} was the word!  YOU WIN!  FROSTY LIVES!⛄️⛄️⛄️")
            return
        
    
play_snowman()
