import random as rand

# import cv2
#
# while True:
#     key = cv2.waitKey(1) & 0xFF
#
#     # if the 'ESC' key is pressed, Quit
#     if key == 27:
#         quit()
#     if key == 0:
#         print("up")
#     elif key == 1:
#         print("down")
#     elif key == 2:
#         print("left")
#     elif key == 3:
#         print("right")
#     # 255 is what the console returns when there is no key press...
#     elif key != 255:
#         print(key)


# positionOfKeys = []
# gameRunning = True
# x = y = 0
#
# # # Returns True if one of the input values is 0
# # # and returns False if none of the values is 0
# def oneIsZero(x, y):
#     if x == 0 or y == 0:
#         return True
#     else:
#         return False
#
# # Spawns keys at different random positions which need to be collected
# # by the player to get to the next level
# def spawnKeys():
#
#     # Global variable to store the position of keys
#     global positionOfKeys
#
#     # Local variables
#     numberOfKeys = 1
#
#     minvalue = -2
#     maxvalue = 2
#
#     # Loop to generate and add number of keys
#     for numberOfKeys in range(0, numberOfKeys):
#         x = rand.randint(minvalue, maxvalue)
#         y = rand.randint(minvalue, maxvalue)
#
#         # Checks if one of the values is zero.
#         while x == 0 or y == 0:
#             if oneIsZero(x, y):
#                 x = rand.randint(minvalue, maxvalue)
#                 y = rand.randint(minvalue, maxvalue)
#
#         positionOfKeys.append((x, y))
#
#     return positionOfKeys
#
#
# def makeMove():
#
#     global x
#     global y
#     # Increment and decrement x and y as per input
#     move = input("Move to : ")
#     if move == "up":
#         y += 1
#     elif move == "down":
#         y -= 1
#     elif move == "right":
#         x += 1
#     elif move == "left":
#         x -= 1
#     else:
#         print("Wrong move! Type right, left, up or down.")
#
#     return x, y
#
#
# keys = spawnKeys()
#
#
# def checkKeys(numberOfKeys):
#
#     global keys
#
#     if numberOfKeys == len(keys):
#         print("ALL THE KEYS HAVE BEEN FOUND")



# spawnKeys()
# def startGame():
#     print("To wander around in this world\n"
#           "Type up, down, right or left\n"
#           "Start roaming and explore !!!\n")
#
#     keyCount = 0
#
#     global keys
#     print(keys)
#
#     while gameRunning:
#         playerPosition = makeMove()
#         for element in keys:
#             if element == playerPosition:
#                 print("A KEY WAS FOUND!!!!")
#                 keyCount += 1
#
#         checkKeys(keyCount)
#
# startGame()
# def printGrid(val):
#     # The grid will always be square
#     # This grid will show the position of the spawned keys of the level
#     gird = []
#     # -x, y -> x++
#     #   |
#     #   V
#     #  y--
#
#     # Creating grid using above logic
#     for x in range(-val, val+1):
#         for y in range(val, -(val-1)):
#             print((i, j))
#             val -= 1
#         print()
#         val += 1
#
# printGrid(2)


# max = 2
# min = -max
#
# currentPositionOfPlayer = (2, 1)
#
# isCorner = False
#
#
# def checkForCorner():
#
#     global currentPositionOfPlayer, max, min
#     global isCorner
#
#     x, y = currentPositionOfPlayer
#     if x == max and y == max:
#         print("You have reached upper right corner")
#         isCorner = True
#     elif x == max and y == min:
#         print("You have reached lower right corner")
#         isCorner = True
#     elif x == min and y == max:
#         print("You have reached upper left corner")
#         isCorner = True
#     elif x == min and y == min:
#         print("You have reached lower left corner")
#         isCorner = True
#
#     return isCorner
#
#
# def checkForEdge():
#
#     global currentPositionOfPlayer, max, min
#     global isCorner
#
#     x, y = currentPositionOfPlayer
#
#     if not isCorner:
#         if x == max:
#             print("You are at the right edge")
#         elif x == min:
#             print("You are at left edge")
#         elif y == max:
#             print("You are at top edge")
#         elif y == min:
#             print("You are at bottom edge")
#     else:
#         quit()
#
#
# def checkPlayerPosition():
#
#     checkForCorner()
#
#     checkForEdge()
#
#
# checkPlayerPosition()


# import keyboard
#
# while True:
#     if keyboard.read_key() == 'q':
#         print("Q was pressed")


# Thia function is called when the player has found all the keys and
# the next round has started
def finalRoundnd():
    pass
    # Create the maze again
    # Add two object at different and random positions (sword and demon)
    # Player will spawn at the center of the maze.
    # Make sure sword or demon are not where the player spawns.
    # movement is the same
    # kill the player and end the game if player finds the demon first
    # player wins if sword is found first
    #


import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True