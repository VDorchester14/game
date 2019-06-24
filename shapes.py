'''
# draw shapes
'''

import pygame as py
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pyramid():
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
    glLineWidth(5.0) # set line width

    glBegin(GL_LINES) # we're about to start drawing lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
