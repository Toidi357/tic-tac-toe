import random
import time
import os
# need to be run on windows command line or windows powershell
os.system("")

def displayBoard(board):
    # modify board to create a temp array
    temp = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]
    for row in range(3):
        for item in range(3):
            if board[row][item] == False:
                temp[row][item] = ' '
            elif board[row][item] == 'x':
                temp[row][item] = 'x'
            elif board[row][item] == 'o':
                temp[row][item] = 'o'
    
    # create output
    line1 = temp[0][0] + " | " + temp[0][1] + " | " + temp[0][2] + '\n---------\n'
    line2 = temp[1][0] + " | " + temp[1][1] + " | " + temp[1][2] + '\n---------\n'
    line3 = temp[2][0] + " | " + temp[2][1] + " | " + temp[2][2] + '\n'

    return '\n' + line1 + line2 + line3

# checks to see if someone won
def evaluate(board):
    # check for 3 in a row
    for row in board:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]
    
    # check for 3 in a column
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return board[0][i]

    # check for diagonal wins
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][0]

    # check if no winner and board is full
    for i in range(3):
        for j in range(3):
            # if one board spot is empty, it means it isn't full and return False
            if board[i][j] == False:
                return False

    return 'No winner'

def userSelection(board, userInput):
    # trim the input
    userInput = userInput.strip()

    # check input
    if len(userInput) != 3 or int(userInput[0]) - 1 > 2 or int(userInput[0]) - 1 < 0 or int(userInput[2]) - 1 > 2 or int(userInput[2]) - 1 < 0:
        return 'Invalid Input'

    # check if specified spot is already taken
    if board[int(userInput[0]) - 1][int(userInput[2]) - 1] != False:
        return 'Spot already taken'

    # make selection and return new board
    board[int(userInput[0]) - 1][int(userInput[2]) - 1] = 'x'
    return board

def computerSelection(board):
    availableOptions = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == False:
                availableOptions.append(str(row) + '-' + str(col))

    choice = random.choice(availableOptions)
    board[int(choice[0])][int(choice[2])] = 'o'
    return board

# for formatting
def pad(text):
    print('\n' + text + '\n')

def main():
    # initialize the board
    board = [
        [False, False, False],
        [False, False, False],
        [False, False, False]
    ]

    pad('don\'t lose, you are "x" the computer is "o"')

    pad(displayBoard(board))

    # loop while no winner
    while evaluate(board) == False:
        selection = userSelection(board, input('Make a selection in this format "row-column", Ex: "1-2": '))
        # error handling
        if selection == 'Invalid Input' or selection == 'Spot already taken':
            pad(selection)
        else:
            board = selection
            time.sleep(1)

            # check if board is full or user won at this point
            if evaluate(board) == 'No winner' or evaluate(board) == 'x':
                break

            # computer selection
            board = computerSelection(board)

            os.system('cls')
            pad(displayBoard(board))

    winner = evaluate(board)

    pad(displayBoard(board))

    if winner == 'x':
        pad('Congrats you won')
    elif winner == 'o':
        pad('You lost')
    else:
        pad('No one won')

if __name__ == '__main__':
    os.system('cls')
    main()
