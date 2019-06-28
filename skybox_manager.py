from my_shaders import cube_vert_shader
from my_shaders import cube_frag_shader

import numpy as np # for vbo arrays

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.arrays import vbo

import sys
from PIL import Image

class skybox():

    vertices = np.array([
    # positions
    -1.0,  1.0, -1.0,
    -1.0, -1.0, -1.0,
     1.0, -1.0, -1.0,
     1.0, -1.0, -1.0,
     1.0,  1.0, -1.0,
    -1.0,  1.0, -1.0,

    -1.0, -1.0,  1.0,
    -1.0, -1.0, -1.0,
    -1.0,  1.0, -1.0,
    -1.0,  1.0, -1.0,
    -1.0,  1.0,  1.0,
    -1.0, -1.0,  1.0,

     1.0, -1.0, -1.0,
     1.0, -1.0,  1.0,
     1.0,  1.0,  1.0,
     1.0,  1.0,  1.0,
     1.0,  1.0, -1.0,
     1.0, -1.0, -1.0,

    -1.0, -1.0,  1.0,
    -1.0,  1.0,  1.0,
     1.0,  1.0,  1.0,
     1.0,  1.0,  1.0,
     1.0, -1.0,  1.0,
    -1.0, -1.0,  1.0,

    -1.0,  1.0, -1.0,
     1.0,  1.0, -1.0,
     1.0,  1.0,  1.0,
     1.0,  1.0,  1.0,
    -1.0,  1.0,  1.0,
    -1.0,  1.0, -1.0,

    -1.0, -1.0, -1.0,
    -1.0, -1.0,  1.0,
     1.0, -1.0, -1.0,
     1.0, -1.0, -1.0,
    -1.0, -1.0,  1.0,
     1.0, -1.0,  1.0
    ])

    def __init__(self, resolution):
        self.resolution = resolution
        return


    def load_box(self):
        textureID = None
        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_CUBE_MAP, textureID)

        # set paths
        path = "assets/purple_night_sky"
        path_modifiers = ["RT.png","LF.png","UP.png","DN.png","FT.png","BK.png"]
        paths = []
        for i, p in enumerate(path_modifiers):
            paths.append(str(path+p))

        # loead textures
        for i, p in enumerate(paths):
            # laod image as chars
            data = Image.open(p).resize((self.resolution,self.resolution)).tobytes()

            if(data):
                # load texture
                glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGB,
                self.resolution, self.resolution, 0, GL_RGB, GL_UNSIGNED_BYTE,
                data)
            else:
                print("Cubemap failed to load")

        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE);
        self.textureID = textureID
        return textureID

    # render the skybox
    def display_box(self):
        vbo = glGenBuffers(1) # make a vbo
        vaos = glGenVertexArrays(1) # make a vao

        # bind and load data
        glBindBuffer(GL_ARRAY_BUFFER, vbo) # bind the vbo
        glBufferData(GL_ARRAY_BUFFER, self.vertices.size, self.vertices, GL_STATIC_DRAW) # load the data

        # create vertex pointers
        glVertexPointer(3, GL_FLOAT, 0, None)

        #glBindVertexArray(vaos)

        glDepthMask(GL_FALSE);
        #skyboxShader.use();
        glBindVertexArray(ass);
        glBindTexture(GL_TEXTURE_CUBE_MAP, self.textureID);
        glDrawArrays(GL_TRIANGLES, 0, 36);
        glDepthMask(GL_TRUE);

        glBindVertexArray(0)
        return
