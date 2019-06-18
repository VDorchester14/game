'''
# draw shapes
'''

import pygame as py
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pyramid(vertices, edges):
    glLineWidth(5.0) # set line width

    glBegin(GL_LINES) # we're about to start drawing lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
