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
    xRot = 16.0
    yRot = 16.0

    def draw_grid(self):
        # GL_LINES pega de dois em dois
        glLineWidth(6)

        # Primeira coluna
        self.draw_line(0, -1, -0.35, 0, 0, 0.02, 2)

        # Segunda coluna
        self.draw_line(0, -1, 0.35, 0, 0, 0.02, 2)

        # Primeira linha
        self.draw_line(-1, 0, 0, -0.35, 0, 2, 0.02)

        # Segunda linha
        self.draw_line(-1, 0, 0, 0.35, 0, 2, 0.02)


    def draw_circle(self, posX, posY):
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)

        glTranslated(tX[posX], tY[posY], 0)
        glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)

        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)

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

        glBegin(GL_QUADS)

        x1 = 0.06
        y1 = -0.14
        x2 = 0.14
        y2 = -0.06

        self.quad_x(x1, y1, x2, y2, y2, x2, y1, x1)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)

        glEnd()

        glMatrixMode(GL_MODELVIEW)

        glRotated(3007 / 16.0, 0.0, 1.0, 0.0)

        glBegin(GL_QUADS)

        self.quad_x(x1, y1, x2, y2, y2, x2, y1, x1)

        self.extrude(x1, y1, x2, y2)
        self.extrude(x2, y2, y2, x2)
        self.extrude(y2, x2, y1, x1)
        self.extrude(y1, x1, x1, y1)

        glEnd()

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

    def extrude(self, x1, y1, x2, y2):
        glVertex3d(x1, y1, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x1, y1, -0.05)

    def quad_x(self, x1, y1, x2, y2, x3, y3, x4, y4):
        glVertex3d(x1, y1, -0.05)
        glVertex3d(x2, y2, -0.05)
        glVertex3d(x3, y3, -0.05)
        glVertex3d(x4, y4, -0.05)

        glVertex3d(x4, y4, +0.05)
        glVertex3d(x3, y3, +0.05)
        glVertex3d(x2, y2, +0.05)
        glVertex3d(x1, y1, +0.05)

    def quad(self, x1, y1, tx, ty):
        glVertex3d(x1, y1, -0.05)
        glVertex3d(x1, y1+ty, -0.05)
        glVertex3d(x1+tx, y1+ty, -0.05)
        glVertex3d(x1+tx, y1, -0.05)

        glVertex3d(x1, y1, 0.05)
        glVertex3d(x1, y1 + ty, 0.05)
        glVertex3d(x1 + tx, y1 + ty, 0.05)
        glVertex3d(x1 + tx, y1, 0.05)

    def draw_line(self, x, y, tx, ty, tz, tamX, tamY):
        glPushMatrix()

        glMatrixMode(GL_MODELVIEW)

        glTranslated(tx, ty, tz)
        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)

        self.quad(x, y, tamX, tamY)

        self.extrude(x, y, -y, -x)
        self.extrude(-y, -x, -x, -y)
        self.extrude(-x, -y, y, x)
        self.extrude(y, x, x, y)

        glEnd()
        glFlush()

        glPopMatrix()

