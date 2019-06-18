'''
Vail Dorchester
'''
# imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pygame as py
from pygame.locals import *

'''
# This class will basically open, update, and close my display
'''
class display_manager():

    # display resolution
    size = [1280, 720]
    disp = None

    # empty init
    def __init__(self):
        return

    # open the display
    def open_display(self):
        py.display.init()
        py.display.set_caption("Game Engine")
        self.disp = py.display.set_mode(self.size, DOUBLEBUF|OPENGL)#, py.FULLSCREEN)

        gluPerspective(45, (self.size[0]/self.size[1]), 0.1, 50)
        glTranslatef(0, 0, -5)

        return

    # update the display
    def update_display(self):
        py.display.flip()
        #py.display.update()
        return

    # close the display
    def close_display(self):
        py.display.quit()
        return
