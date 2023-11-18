# 1. Name:
#      Jesse Earley 
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This program takes a soduku game from a json and prints it on the screen
#       You can chose a spot to add a number and save your game
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was trying to figure out how to best display the board from the json.
#       It has been a while since I have had to use json in python so I had to go learn it again.
# 5. How long did it take for you to complete the assignment?
#      3 Hours

import json
#calls 3 functions read_board(), play_round(), write_board() 
def main():
    game_over = False
    board = False
    while board == False:       
        board = read_board()
    
    while not game_over:        
        display_board(board)
        game_option = play_round(board)
        if  game_option == "Q":
            write_board(board)
            game_over = True
        elif game_option == "S":
            coordinates = get_coordinate(board, True)
            column = coordinates[0]
            row = coordinates[1]
            print(f'Possible values for {column}{row}:{show_possible_values(board, column, row)}')
        check_game_over(board)

def check_game_over(board):
    for row in board:
        for value in row:
            if value == " ":
                return False
    return True

#No functions called
def display_board(board):
    print('   A B C D E F G H I')
    for i in range(9):
        if i % 3 == 0 and i != 0 :
            print('   -----+-----+-----')
        row = '{}  {} {} {}|{} {} {}|{} {} {}'
        print(row.format(i + 1, board[i][0],board[i][1],board[i][2],board[i][3],board[i][4],board[i][5],board[i][6],board[i][7],board[i][8]))

#No functions Called
def read_board():
    print('Welcome to Sudoku!\n'
          'Please Select from the following the desired difficulty\n'
          '1: Easy\n'
          '2: Medium\n'
          '3: Hard\n'
          '4: Previously saved game')
    selection = int(input('Selection: '))
    
    if selection == 1 :
        game_file = '131.05.Easy.json'
    elif selection == 2:
        game_file = '131.05.Medium.json'
    elif selection == 3:
        game_file = '131.05.Hard.json'
    elif selection == 4:
        game_file = 'saved_game.json'
    try:
        file = open(game_file, "r")
        data = json.loads(file.read())
        board = data["board"]
        file.close()
        
    except:
        print('\nNo previously saved file\n')
        return False
    x_index = 0
    
    #Iterates through each number and changes it from a zero to a space
    for x in board:
        y_index = 0
        for y in x:
            if y == 0:
                board[x_index][y_index] = " "
            y_index += 1
        x_index += 1
        
    return board

#Calls get_coordinate(), get_number(), is_input_legal
def play_round(board):
    coordinates = get_coordinate(board)
    
    if len(coordinates) == 1:
        #Handles the Quit and S to Show all possible values
        if coordinates == 'Q' or coordinates == 'S':
            return coordinates
    
    #Handles Coordinate input
    column = coordinates[0]
    row = coordinates[1]
    row_index = row - 1
    valid_num = False
    while not valid_num:
        try:
            number = int(input(f'What number goes in {column}{row}: '))
        except:
            print('That is not a valid number')
            continue
        if is_input_legal(board, row, column, number) and validate_row(number):
            valid_num = True
            column_index = get_column_index(column)
            board[row_index][column_index] = number
            return board
        else:
            print(f'{number} will not work in {column}{row}')

#calls validate_options(), validate_row(), validate_column()
def get_coordinate(board, view_possible_values = False):
    is_valid_coordinate = False
    while not is_valid_coordinate:
        if view_possible_values:
            coordinate = input('\nSpecify a coordinate you want to see possible values for:  ')
        else:
            coordinate = input('\nSpecify a coordinate to edit or \'Q\' to save and quit Example \'B2\': ')
        #checks to make sure there is a Letter number pair 
        if len(coordinate) == 1:
            coordinate = validate_options(coordinate)
            if coordinate == "Q" or coordinate == "S":
                return coordinate
            else:
                print(f'{coordinate} is not a valid option!')
                
        elif len(coordinate) == 2:
            #validate coordinates
            try:
                row = int(coordinate[1])
                column = str(coordinate[0])
            except:
                try:
                    row = int(coordinate[0])
                    column = str(coordinate[1])
                except:
                    print(f'{coordinate} is not a valid selection')
                    return            
            
            if validate_row(row):
                if validate_column(column):
                    print(f'{column} {row}')            
                    return column, row
                
        else:
            print(f'{coordinate} is not a valid option\n')

#No functions called
def validate_options(option):
    option = option.upper()
    if option == 'Q':
        return option
    
    #Handles S to Show all possible values
    elif option == 'S':
        return option
    
    else:
        return option

#No functions called
def validate_row(row):
    if int(row) > 9 or int(row) < 1:
        print(f'{row} is not a valid row Select a row between 1 and 9\n')
        return
    else:
        return True

#No functions called
def validate_column(column):
    column = column.upper()
    if column < 'A' or column > 'I':
        print(column.upper())
        print('Please select a letter between A and I: ')
        return
    else:
        return True

def get_column_index(column):
    column = column.upper()
    if column == "A":
        return 0
    elif column == "B":
        return 1
    elif column == "C":
        return 2
    elif column == "D":
        return 3
    elif column == "E":
        return 4
    elif column == "F":
        return 5
    elif column == "G":
        return 6
    elif column == "H":
        return 7
    elif column == "I":
        return 8

def validate_coordinate(coordinate):
    pass

#Calls is_square_filled(), unique_row(), unique_column(), unique_inside_square()
def is_input_legal(board, row, column, number):
    if is_square_filled(board, row, column):
        return False
    elif unique_row(board, row, number):
        return False
    elif unique_column(board, column, number):
        return False
    elif unique_inside_square(board, row, column, number):
        return False
    else:
        return True

#Calls get_column_index()
def is_square_filled(board, row, column):
    row_index = int(row) - 1
    column_index = get_column_index(column)
    if board[row_index][column_index] != " ":
        return True

def unique_row(board, row, number):
      row_index = int(row) - 1
      if number in board[row_index]:
          return True

#Calls get_column_index()
def unique_column(board, column, number):

    column_index = get_column_index(column)
    for row in board:
        if row[column_index] == number:
            return True

#Calls get_column_index()
def unique_inside_square(board, row, column, number):
    row_index = int(row) - 1
    if row_index < 3:
        row_quadrant = [0,1,2]
    elif row_index > 5:
        row_quadrant = [6,7,8]
    else:
        row_quadrant = [3,4,5]
        
    column_index = get_column_index(column)
    if column_index < 3:
        column_quadrant = [0,1,2]
    elif column_index > 5:
        column_quadrant = [6,7,8]
    else:
        column_quadrant = [3,4,5]
        
    for row in row_quadrant:
        for column in column_quadrant:
            if board[row][column] == number:
                return True
            
# Calls is_input_legal
def show_possible_values(board, column, row):
    valid_numbers = []
    for number in range(1,10):        
        if is_input_legal(board, row, column, number):
            valid_numbers.append(number)
    return valid_numbers

def write_board(board):
    #Iterates through each number and changes it from a space to a zero
    x_index = 0
    for x in board:
        y_index = 0
        for y in x:
            if y == " ":
                board[x_index][y_index] = 0
            y_index += 1
        x_index += 1
        
    board = {"board":board}
    data = json.dumps(board)
    file = open("saved_game.json", "w")
    file.write(data)
    file.close()

if __name__ == '__main__':
    main()