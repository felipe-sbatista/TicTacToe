import numpy
from OpenGL.GL import *
import math
import env

class Drawer():
    def draw_grid(self):
        # GL_LINES pega de dois em dois
        glBegin(GL_LINES)

        # Vertical

        # Primeira coluna
        glVertex2f(.33, 1)
        glVertex2f(.33, -1)

        # Segunda coluna
        glVertex2f(-.33, 1)
        glVertex2f(-.33, -1)

        # Horizontal

        # Primeira linha
        glVertex2f(1, .33)
        glVertex2f(-1, .33)

        # Segunda linha
        glVertex2f(1, -.33)
        glVertex2f(-1, -.33)

        glEnd()
        glFlush()

    def draw_circle(self, radius):
        # LINE LOOP pega linhas interligadas, no caso nosso circulo
        glLineWidth(6)
        glBegin(GL_LINE_LOOP)

        deg = 3.1415/180
        radius = -.2
        for i in range(360):
            rad = deg*i
            glVertex2f(math.cos(rad)*radius,math.sin(rad)*radius)

        #aqui da ruim
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(2, 0, 0)

        glEnd()
        glFlush()

    # position contem o quadrante que vamos marcar
    def draw_x(self, position):
        pass

