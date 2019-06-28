from OpenGL.GL import *
from OpenGL.arrays import vbo
#from OpenGLContext.arrays import *
from OpenGL.GL import shaders
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GL import glCreateShader

bVERTEX_SHADER = """
        #version 120
        void main() {
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        }
        """
print(bool(glCreateShader))
vertexShader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertexShader, VERTEX_SHADER)
