from random import randint

MAX_TURNS = 5
board = []

# Our board will be a 5x5 grid of "O"s
for x in range(5):
    board.append(["O"] * 5)

#To help make things prettier
def printLine():
    print("\n")

# Method to print our board
def print_board(board):
    print("  1 2 3 4 5")
    for row in range(len(board)):
        print( row+1, " ".join(board[row]))

printLine()
print( "Let's play Battleship!" )
print( "You have", MAX_TURNS, "turns.")
print("My battleship is hidden somewhere in this ocean!")
print("Try and sink it!")
printLine()
print_board(board)
printLine()

# Generate a random location for the battleship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# initialize the location of the ship
ship_row = random_row(board)
ship_col = random_col(board)

# print our location for debugging puposes only
#print(ship_row+1)
#print(ship_col+1)

gameOver = False

# Total of MAX_TURNS turns
for turn in range(MAX_TURNS):
    if( MAX_TURNS - turn == 1 ):
        print("You have 1 turn remaining.")
    else:
        print("You have", MAX_TURNS - turn, "turns remaining.")

    #get the user's guess
    guess_row = int(input("Guess Row:    ")) - 1
    guess_col = int(input("Guess Column: ")) - 1
    printLine()

    #if the guess is right
    if guess_row == ship_row and guess_col == ship_col:
        board[ship_row][ship_col] = "^"
        print_board(board)
        print("Congratulations! You sunk my battleship!")
        break

    #cases for when the guess is wrong
    else:
        if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")

        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        if( turn == MAX_TURNS - 1 ):
            print_board(board)
            print("Out of turns, game Over :(")
            printLine()
            gameOver = True

    #re-print for the next turn
    if( not gameOver ):
        printLine()
        print("--------------------------------------")
        print("Try again!")
        printLine()
        print_board(board)
        printLine()