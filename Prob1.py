############################################################
# Name:Jack Crone
# Name(s) of anyone worked with:Cody Pagone
# Est time spent (hr):0.5
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

def draw_swedish_flag():

    gw = GWindow(800, 600)

    # blue background 
    background = GRect(0, 0, 800, 600)
    background.set_filled(True)
    background.set_fill_color('#005eb8')  
    gw.add(background)

    # vertical part of the yellow cross
    vertical_cross = GRect(240, 0, 80, 600)
    vertical_cross.set_filled(True)
    vertical_cross.set_fill_color('#fecc00')  
    gw.add(vertical_cross)

    # horizontal part of the yellow cross
    horizontal_cross = GRect(0, 240, 800, 80)
    horizontal_cross.set_filled(True)
    horizontal_cross.set_fill_color('#fecc00')  
    gw.add(horizontal_cross)

draw_swedish_flag()
