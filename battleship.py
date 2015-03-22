from random import randint

MAX_TURNS = 10
TOTAL_SHIPS = 5
ROW = 0
COLUMN = 1

board = []
ships = []

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

# 
# Param: ships, empty list of ships
# Param: board 
# Mutates: ships, adds a unique ship to the list of ships
def createShip(ships, board):
    shipRow = random_row(board)
    shipCol = random_col(board)
    ship = [shipRow, shipCol]

    if ship not in ships:
        ships.append(ship)
    else:
        createShip(ships, board)

# initialize the random location of our ships
for numberOfShips in range(TOTAL_SHIPS):
    createShip(ships, board)

# print our location for debugging puposes only
#print(ship_row+1)
#print(ship_col+1)

gameOver = False

#to keep track of how many ships we have sunk
sunken = 0

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
    for ship in ships:
        ship_row = ship[ROW]
        ship_col = ship[COLUMN]

        if guess_row == ship_row and guess_col == ship_col:
            board[ship_row][ship_col] = "^"
            print_board(board)
            print("You sunk one of my battleships!")
            sunken += 1

            if( sunken == TOTAL_SHIPS):
                printLine()
                print("Congratulations you have sunk all my ships!")
                print("YOU WIN! :)")
                break

            print("There are", TOTAL_SHIPS - sunken, "ships left!")


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