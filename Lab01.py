# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json
import os

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '
save_file = 'save.json'
# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }
#done
def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    if os.path.exists(f'./{filename}'):
        f = open(filename)
        board = json.load(f)
        f.close()
        return board['board']
    return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    f = open(filename, "w")
    save_info = {"board": board}
    json.dump(save_info, f)
    f.close()

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    x_count = 0
    for i in board:
        if i != BLANK:
            x_count += 1
    if x_count % 2 != 0:
        return False
    return True

def make_selection(player):
        selection = input(f"It is {player}'s turn:")
        if selection == "q":
            save_board(save_file,board)
            print('Game Successfully Saved!!!')
            return False
        else:
            selection = int(selection)
            
        if board[selection - 1] == BLANK:
            board[selection - 1] = player
        else:
            print("That spot is already taken please choose another")
        return True
def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    display_board(board)
    #X's turn 
    if is_x_turn(board):
        if not make_selection(X):
            return False
        
    #O's Turn
    else:
        if not make_selection(O):
            return False
    #check if game is done    
    if game_done(board, True):
        # if game is done reset the board
        save_board(save_file,blank_board["board"])
        return False
    return True

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

#done
# The file read code, game loop code, and file close code goes here.
if __name__ == "__main__":
    board = read_board(save_file)
    while play_game(board):
        pass
    