import numpy
from OpenGL.GL import *
import math
import env

posSquare = 0.33
posCircle = posSquare * 2

tX = [-posCircle, 0, posCircle]
tY = [posCircle, 0, -posCircle]

class Drawer():
    def draw_grid(self):
        # GL_LINES pega de dois em dois
        glBegin(GL_LINES)

        # Vertical

        # Primeira coluna
        glVertex2f(posSquare, 1)
        glVertex2f(posSquare, -1)

        # Segunda coluna
        glVertex2f(-posSquare, 1)
        glVertex2f(-posSquare, -1)

        # Horizontal

        # Primeira linha
        glVertex2f(1, posSquare)
        glVertex2f(-1, posSquare)

        # Segunda linha
        glVertex2f(1, -.33)
        glVertex2f(-1, -.33)

        glEnd()
        glFlush()

    def draw_circle(self, posX, posY):
        glLineWidth(6)
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)
        glTranslatef(tX[posX], tY[posY], 1)

        # LINE LOOP pega linhas interligadas, no caso nosso circulo
        glBegin(GL_LINE_LOOP)

        deg = 3.1415 / 180
        radius = -.2
        for i in range(360):
            rad = deg * i
            glVertex2f((math.cos(rad) * radius), math.sin(rad) * radius)

        glEnd()
        glFlush()

        glPopMatrix()
    # position contem o quadrante que vamos marcar
    def draw_x(self, position):
        pass

