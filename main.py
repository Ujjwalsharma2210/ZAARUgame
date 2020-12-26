import random as rand
# import time

# ----GLOBAL----
positionOfKeys = []

currentPositionOfPlayer = ()

# Size of grid
max = 3
min = 3

# Initial position of player
x = y = 0

# State of the game : Running or not
gameRunning = True

# def printGrid():


# Returns True if one of the input values is 0
# and returns False if none of the values is 0
def oneIsZero(x, y):
    if x == 0 or y == 0:
        return True
    else:
        return False

# Spawns keys at different random positions which need to be collected
# by the player to get to the next level
def spawnKeys():

    # Global variable to store the position of keys
    global positionOfKeys

    # Local variables
    numberOfKeys = 3

    minvalue = -3
    maxvalue = 3

    # Loop to generate and add number of keys
    for numberOfKeys in range(0, numberOfKeys):
        x = rand.randint(minvalue, maxvalue)
        y = rand.randint(minvalue, maxvalue)

        # Checks if one of the values is zero.
        while x == 0 or y == 0:
            if oneIsZero(x, y):
                x = rand.randint(minvalue, maxvalue)
                y = rand.randint(minvalue, maxvalue)

        positionOfKeys.append((x, y))

    return positionOfKeys

# Everytime the player makes a move this function return values of x and y
def makeMove():

    global x
    global y
    # Increment and decrement x and y as per input
    move = input("Move to : ")
    if move == "up":
        y += 1
    elif move == "down":
        y -= 1
    elif move == "right":
        x += 1
    elif move == "left":
        x -= 1
    else:
        print("Wrong move! Type right, left, up or down.")

    return x, y

# Runs the game
def startGame():
    print("To wander around in this world\n"
          "Type up, down, right or left\n"
          "Start roaming and explore !!!\n")

    keys = spawnKeys()
    while gameRunning:
        position = makeMove()
        if position in keys:
            pass

# main function Which asks to start the game
def playGame():
    playerName = input("\nHello wanderer! What's your name?\n")
    print()
    print("Hello " + playerName + ", Welcome to the world of blocks!\n"
          "This world is cursed by the demon king ZAARU, You are sent here to save us\n"
          "The person who comes here can only move up, down, right or left by making a wish.\n"
          "Collect the keys and open doors to find relics which will help you to defeat the demon...\n"
          "Are you ready for the adventure?")
    print()
    initiation = input("Enter y or n : ")
    if initiation == "y":
        startGame()
    elif initiation == "n":
        print("Come prepared next time!\n"
              "We need you")
        exit()


playGame()

# Current position
# path or previous positions the player has been in.
