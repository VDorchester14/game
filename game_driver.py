# Vail Dorchester

from display_manager import display_manager
from menu_manager import menu_manager
from shapes import pyramid

import pygame as py
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


'''
# This class drives the game and display manager
'''
class game_driver():
    dm = None # set empty pointer to display manager opbject
    mm = None # empty menu manager
    load = None
    render = None

    # empty init
    def __init__(self):
        return

    # run the game
    def run(self):
        # create a display manager and open the display
        self.dm = display_manager()
        self.dm.open_display()


        # open and run the main menu
        #self.main_menu()

        vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (0, 0, 1)
        )

        edges = (
        (0,1),
        (0,3),
        (0,4),
        (1,4),
        (1,2),
        (2,4),
        (2,3),
        (3,4)
        )

        # show the game until the user tries to exit
        clock = py.time.Clock()
        running = True # to tell if the game is running
        while(running):
            clock.tick(60)

            # render
            glRotatef(2,1,1,3)
            pyramid(vertices, edges)


            # update the display
            self.dm.update_display()

            # see if it's still running
            for event in py.event.get(): # for events
                if event.type == py.QUIT: # if they try to quit
                    py.quit()
                    quit()
                '''# check if esc key
                if event.tpye == py.KEYDOWN:
                    if event.key == py.K_ESCAPE:
                        running = False'''
            # clear
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # close the display
        self.dm.close_display()
        return

    # a wrapper class to open the main menu
    def main_menu(self):
        self.mm = menu_manager(self.dm)
        self.mm.main_menu()
        return

'''
Main method
'''
def main():
    driver = game_driver()
    driver.run()
    return -1

if __name__=='__main__':
    main()
