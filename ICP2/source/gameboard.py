# ICP2
print('Program to show Game Board')


def board_draw(height, width):
    # Initialising Board Parameter
    board = ""
    # Getting the Size using height and width

    # Iterating the boardSize using range function
    for ran in range(height):

     board = board+" ---" * (width) + "\n"
     for x in range(width):
         board = board+"|   "
     board = board + "|   \n"

    # Finally, adding the Horizontal lines at the end
    board = board + " ---" * (width)
    return board



# Getting Inputs from the User
heightInput = int(input("Enter the height of the board: "))
widthInput = int(input("Enter the width of the board: "))

# Calling a function to show the Game Board based on height and width
print(board_draw(heightInput, widthInput))
