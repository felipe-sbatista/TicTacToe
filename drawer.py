from PySide2.QtWidgets import QHBoxLayout, QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QOpenGLWidget, QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *
from OpenGL.GL import *
import math

posSquare = 0.33
posCircle = posSquare * 2
POSX = posSquare / 2

tX = [-posCircle, 0, posCircle]
tY = [posCircle, 0, -posCircle]


class Drawer():
    def draw_grid(self):
        # GL_LINES pega de dois em dois
        glLineWidth(6)
        glBegin(GL_LINES)
        glColor3f(1, 1, 1)

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
        glVertex2f(1, -posSquare)
        glVertex2f(-1, -posSquare)

        glEnd()
        glFlush()

    def draw_circle(self, posX, posY):
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)

        glTranslated(tX[posX], tY[posY], 0)

        glBegin(GL_QUADS)

        NumSectors = 200
        x1Const = 0.15
        x2Const = 0.10
        for i in range(NumSectors):
            angle1 = (i * 2 * math.pi) / NumSectors
            x5 = x1Const * math.sin(angle1)
            y5 = x1Const * math.cos(angle1)
            x6 = x2Const * math.sin(angle1)
            y6 = x2Const * math.cos(angle1)

            angle2 = ((i + 1) * 2 * math.pi) / NumSectors
            x7 = x2Const * math.sin(angle2)
            y7 = x2Const * math.cos(angle2)
            x8 = x1Const * math.sin(angle2)
            y8 = x1Const * math.cos(angle2)

            self.draw_faces(x5, y5, x6, y6, x7, y7, x8, y8)

            self.draw_shadows(x6, y6, x7, y7)
            self.draw_shadows(x8, y8, x5, y5)

        glEnd()
        glFlush()

        glPopMatrix()

    def draw_x(self, posX, posY):
        glLineWidth(6)
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)
        glTranslatef(tX[posX], tY[posY], 0)

        glBegin(GL_LINES)

        glVertex2f(0, 0)
        glVertex2f(POSX, -POSX)

        glVertex2f(0, 0)
        glVertex2f(-POSX, -POSX)

        glVertex2f(0, 0)
        glVertex2f(POSX, POSX)

        glVertex2f(0, 0)
        glVertex2f(-POSX, POSX)

        glEnd()
        glFlush()

        glPopMatrix()

    def draw_faces(self, x1, y1, x2, y2, x3, y3, x4, y4):
        glVertex3d(x1, y1, -0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x3, y3, -0.05)
        glVertex3d(x4, y4, -0.05)

        glVertex3d(x4, y4, +0.05)
        glVertex3d(x3, y3, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x1, y1, +0.05)

    def draw_shadows(self, x1, y1, x2, y2):
        glVertex3d(x1, y1, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x1, y1, -0.05)
