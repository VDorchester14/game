from OpenGL.GL import *
from OpenGL.arrays import vbo
#from OpenGLContext.arrays import *
from OpenGL.GL import shaders
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import glCreateShader

class cube_vert_shader():

    def __init__(self):
        self.VERTEX_SHADER = shaders.compileShader("""
        #version 330 core
        layout (location = 0) in vec3 aPos;

        out vec3 TexCoords;

        uniform mat4 projection;
        uniform mat4 view;

        void main()
        {
            TexCoords = aPos;
            gl_Position = projection * view * vec4(aPos, 1.0);
        }
        """, GL_VERTEX_SHADER)
        return

class cube_frag_shader():

    def __init__(self):
        self.FRAGMENT_SHADER = shaders.compileShader("""
        #version 330 core
        out vec4 FragColor;

        in vec3 TexCoords;

        uniform samplerCube skybox;

        void main()
        {
            FragColor = texture(skybox, TexCoords);
        }
        """, GL_FRAGMENT_SHADER)
        return
