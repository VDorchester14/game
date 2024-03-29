'''
# draw shapes
'''

import pygame as py
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

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

def triangle():
    vertices = np.array([
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0, 0.5, 0.0
    ])
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, len(vertices), vertices, GL_STATIC_DRAW)
    return
