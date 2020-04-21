from PySide2.QtWidgets import QHBoxLayout, QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QOpenGLWidget, QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *
from OpenGL.GL import *
import env
from drawer import Drawer
from typing import List
DRAWER = Drawer()


class Positions():
    x = 0;
    y = 0;


class Game(QOpenGLWidget):
    selectedCoordinates: List[Positions] = []

    def __init__(self, QOpenGLWidget):
        super().__init__()

    def initializeGL(self):
        self.setFixedSize(QSize(env.VIEW_WIDTH, env.VIEW_HEIGHT))
        glViewport(0, 0, env.VIEW_WIDTH, env.VIEW_HEIGHT)

    def calculateCoordinates(self, x, y):
        coordinates = Positions()
        # identifying x index
        if 0 <= x < 211:
            coordinates.x = 0
        elif 218 <= x < 423:
            coordinates.x = 1
        else:
            coordinates.x = 2

        # identifying y index
        if 0 <= y < 157:
            coordinates.y = 0
        elif 166 <= y < 316:
            coordinates.y = 1
        else:
            coordinates.y = 2

        return coordinates

    def mouseReleaseEvent(self, QMouseEvent):
        positions = self.calculateCoordinates(QMouseEvent.x(), QMouseEvent.y())
        print("x: " + str(positions.x) + " Y: " + str(positions.y))
        self.selectedCoordinates.append(positions)
        self.repaint()

    def repaint(self):
        for coordinate in self.selectedCoordinates:
            DRAWER.draw_circle(coordinate.x, coordinate.y)
        self.update()

    def paintGL(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1, 0.67, 0.30, 1.0)
        glPointSize(10)
        DRAWER.draw_grid()
        self.repaint()

