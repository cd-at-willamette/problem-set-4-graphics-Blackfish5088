########################################
# Name:Jack Crone
# Collaborators:Cody Pagone
# Estimated time spent (hrs):1
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600

# Constants
BRICK_WIDTH = 40       # Width of each brick
BRICK_HEIGHT = 20      # Height of each brick
BRICKS_IN_BASE = 10    # Number of bricks in the base row

# Function to draw the pyramid
def draw_pyramid():
    
    gw = GWindow(400, 300)
    

    window_width = gw.get_width()
    window_height = gw.get_height()
    
    base_y = window_height - BRICK_HEIGHT
    

    for row in range(BRICKS_IN_BASE):
        
        num_bricks = BRICKS_IN_BASE - row
        
       
        start_x = (window_width - num_bricks * BRICK_WIDTH) / 2
        y = base_y - row * BRICK_HEIGHT  
        

        for brick in range(num_bricks):
            x = start_x + brick * BRICK_WIDTH
            rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            rect.set_filled(True)
            rect.set_fill_color("pink")  
            gw.add(rect)


draw_pyramid()














if __name__ == '__main__':
    draw_pyramid()
