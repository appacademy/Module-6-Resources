import os
from game_info import board, score, moves, board_matrix, past_moves


# 1. Draw the game board
# 2. Ask the player for input
# 3. Determine if the input is valid
# 4. Update game state
# 5. Redraw our game board
# 6. Update score
# 7. Determine if the game is over
# 8. Iterate through the previous steps (changing the current player each time)


def main(board, score, moves, board_matrix, past_moves):
    print("Welcome to Tic Tac Toe! Let's start the game!")
    input("Please hit enter to start playing...")

    print(draw_board(board, board_matrix))

    move_number = 1

    while True:
        player = "X" if move_number % 2 == 1 else "O"
        spot = prompt_for_move(player)
        while not check_move(spot, past_moves, board_matrix, moves):
            spot = prompt_for_move(player)
        board_matrix = update_game_state(spot, moves, board_matrix, player)
        print(draw_board(board, board_matrix))
        score = update_score(spot, moves, score, player)
        winner = check_for_winner(score)
        winner = end_game(winner, move_number)
        if winner:
            break
        move_number += 1


    

def draw_board(board, board_matrix):
    os.system("clear")
    new_board = ""
    x, y = 0, 0
    for char in board:
        if char.isnumeric():
            if board_matrix[x][y]:
                char = board_matrix[x][y]
            if y == 2:
                y, x = 0, x+1
            else:
                y += 1
        new_board += char
    return new_board

def prompt_for_move(player):
    spot = input(f"It's your turn, {player}! Enter a position to place your marker: ")
    return spot

def check_move(spot, past_moves, board_matrix, moves):
    if not spot.isnumeric() or not 0 < int(spot) < 10:
        print("Please enter a valid value")
        return False
    move_x, move_y = moves[spot]
    if board_matrix[move_x][move_y]:
        print("This space has already been taken. Please enter a new value")
        return False
    return True

def update_game_state(spot, moves, board_matrix, player):
    move_x, move_y = moves[spot]
    board_matrix[move_x][move_y] = player
    return board_matrix



def update_score(spot,moves, score, player):
    move = moves[spot]
    new_score = { **score }
    new_score[move[0], None][player] += 1
    new_score[None, move[1]][player] += 1
    if move[0] == move[1]:
        new_score["diag_1"][player] += 1
    if move[0] + move[1] == 2:
        new_score["diag_2"][player] += 1
    return new_score
    

def check_for_winner(score):
    winner = None
    for line in score.values():
        if line["X"] == 3:
            winner = "X"
        elif line["O"] == 3:
            winner = "O"
    return winner

def end_game(winner, move_number):
    if winner == "X" or winner == "O":
        print(f"Congrats, {winner}! You've won!!!")
    elif move_number == 9:
        print("You two are very well-matched! It's a tie!!!!")
        winner = True
    return winner



if __name__ == "__main__":
    main(board, score, moves, board_matrix, past_moves)
