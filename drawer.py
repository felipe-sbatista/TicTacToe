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
        glLineWidth(6)
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)
        glTranslatef(tX[posX], tY[posY], 0)

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

    def draw_home(self):
        glBegin(GL_QUADS)

        # glDraw
        glColor3f(2/255, 195/255, 154/255)
        # glColor3f(5/255, 102/255, 141/255)
        glVertex2f(-posSquare, posSquare/2)
        glVertex2f(-posSquare, -posSquare/2)
        glVertex2f(posSquare, -posSquare/2)
        glVertex2f(posSquare, posSquare/2)

        glEnd()
        glFlush()

        label = QLabel()
        label.setText("Hello")
        label.setAlignment(Qt.AlignCenter)
