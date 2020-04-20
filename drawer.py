import numpy
from OpenGL.GL import *
import OpenGL.GL.shaders

class Drawer():
    def draw_grid(self):
        # glClear(GL_COLOR_BUFFER_BIT)
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(1.0, 0.0, 0.0)
        ysize = 0
        for i in range(3):
            xsize = 0
            for j in range(3):
                glBegin(GL_POLYGON)
                glVertex3f(-50.0 + xsize, -50.0 + ysize, 0.0)
                glVertex3f(-40.0 + xsize, -50.0 + ysize, 0.0)
                glVertex3f(-40.0 + xsize, -40.0 + ysize, 0.0)
                glVertex3f(-50.0 + xsize, -40.0 + ysize, 0.0)
                glEnd()
                xsize += 3.0

            ysize += 3.0

        glFlush()

    def draw_rect(self):
        pass
