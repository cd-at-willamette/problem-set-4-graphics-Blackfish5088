########################################
# Name:Jack Crone
# Collaborators:Cody Pagone
# Estimate time spent (hrs):1
########################################

from pgl import GWindow, GRect, GLabel
import random

# Constants
GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'arial'"    # Font for score

def clicky_box():
    # Create the graphics window 
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    # Create a filled square 
    square = GRect(SQUARE_SIZE, SQUARE_SIZE)
    square.setFilled(True)
    square.setColor('pink')  # You can choose any color you like
    center_x = (GW_WIDTH - SQUARE_SIZE) / 2
    center_y = (GW_HEIGHT - SQUARE_SIZE) / 2
    gw.add(square, center_x, center_y)

    # Initialize the score and create a label 
    score = 0
    score_label = GLabel(f"{score}")
    score_label.setFont(SCORE_FONT)
    label_x = SCORE_DX
    label_y = GW_HEIGHT - SCORE_DY
    gw.add(score_label, label_x, label_y)

    # Store variables 
    gw.square = square
    gw.score = score
    gw.score_label = score_label

    # mouse click event handler
    def on_mouse_down(event):
        x = event.getX()
        y = event.getY()
        square = gw.square

        # Check if the click was inside the square
        square_x = square.getX()
        square_y = square.getY()
        if (square_x <= x <= square_x + SQUARE_SIZE) and (square_y <= y <= square_y + SQUARE_SIZE):
            # Increase the score
            gw.score += 1

            # Move the square to a new position
            max_x = GW_WIDTH - SQUARE_SIZE
            max_y = GW_HEIGHT - SQUARE_SIZE
            new_x = random.uniform(0, max_x)
            new_y = random.uniform(0, max_y)
            square.setLocation(new_x, new_y)
        else:
            # Reset the score
            gw.score = 0

        # Update the score label
        gw.score_label.setLabel(f"{gw.score}")

    # Add the mouse event listener 
    gw.addEventListener('mousedown', on_mouse_down)

# Run the function
if __name__ == "__main__":
    clicky_box()
