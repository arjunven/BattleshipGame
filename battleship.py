from random import randint

# define constants
MAX_TURNS = 10
TOTAL_SHIPS = 5
ROW = 0
COLUMN = 1
OCEAN = "O"
MISS = "X"
HIT = "*"

board = []
ships = []

# Our board will be a 5x5 grid of "O"s
for x in range(5):
    board.append([OCEAN] * 5)

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
print("There are", TOTAL_SHIPS, "battleships hidden somewhere in this ocean!")
print("Try and sink them all!")
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

# initialize the random locations of our ships
for numberOfShips in range(TOTAL_SHIPS):
    createShip(ships, board)

# print the solutions for debugging/testing puposes only
for ship in ships:
    print(ship)

# Checks to see if the user's guess has hit a ship
#
# Param: ships, list of all the ships
# Param: board, mutates the board to show where a ship was hit
# Param: guess_row
# Param: guess_col
#
# Returns: True if a ship is Hit and false otherwise
def hit(ships, board, guess_row, guess_col):
    for ship in ships:
        if(guess_row == ship[ROW] and guess_col == ship[COLUMN]):
            board[ship[ROW]][ship[COLUMN]] = HIT
            return True

    return False


gameOver = False

#to keep track of how many ships we have sunk
sunken = 0

# Total of MAX_TURNS turns
for turn in range(MAX_TURNS):
    #to keep track if ship was sunk or not this turn
    #used for print formatting if previous move was a hit
    sunkOne = False

    if( MAX_TURNS - turn == 1 ):
        print("You have 1 turn remaining.")
    else:
        print("You have", MAX_TURNS - turn, "turns remaining.")

    #get the user's guess
    guess_row = int(input("Guess Row:    ")) - 1
    guess_col = int(input("Guess Column: ")) - 1
    printLine()

    #if the user has hit a ship
    if( hit(ships, board, guess_row, guess_col) ):
        sunken += 1
        sunkOne = True

        #if the user has sunk all the ships they have won
        #ends the game
        if( sunken == TOTAL_SHIPS):
            print("NOOOooOOO you have sunk all my ships!")
            print("YOU WIN THIS BATTLE!")
            break

        print("You sunk one of my battleships!")
        
        #otherwise we inform them how many ships are left
        if( sunken == TOTAL_SHIPS - 1 ):
            print("There is only 1 ship left!")
        else:
            print("There are", TOTAL_SHIPS - sunken, "ships left.")



    #cases for when the guess is wrong (no ships hit)
    else:
        if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")

        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")

        else:
            print("You missed!")
            board[guess_row][guess_col] = MISS

        if( turn == MAX_TURNS - 1 ):
            printLine()
            print_board(board)
            printLine()
            print("Out of turns, game Over :(")
            gameOver = True

    #re-print for the next turn
    if( not gameOver ):
        printLine()
        print("--------------------------------------")
        if( sunkOne ):
            printLine()
            print( "You may have gotten lucky this time...")
            print( "but you won't find the rest of them!")
        else:
            print("Try again!")
        printLine()
        print_board(board)
        printLine()