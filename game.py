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
    x = 0
    y = 0

class Game(QOpenGLWidget):
    selectedCoordinates: List[Positions] = []
    SCREEN = 1

    def __init__(self, QOpenGLWidget):
        super().__init__()
        '''
        if turn equals to false, then cirlcle will be marked
        and if its equals to true, then X will be marked 
        '''
        self.turn = False

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

    def calculateCoordinatesHome(self, x, y):
        print(x, y, 215 <= x < 426, 204 <= y < 280)
        if 215 <= x < 426 and 204 <= y < 280:
            return 2
        return 1

    def checkPlayPosition(self, x, y):
        for coordinate in self.selectedCoordinates:
            if coordinate.x == x and coordinate.y == y:
                print("this field has been already choosen")
                return False
        return True

    def mouseReleaseEvent(self, QMouseEvent):
        if self.SCREEN == 1:
            self.SCREEN = self.calculateCoordinatesHome(QMouseEvent.x(), QMouseEvent.y())
        elif self.SCREEN == 2:
            positions = self.calculateCoordinates(QMouseEvent.x(), QMouseEvent.y())
            print("x: " + str(positions.x) + " Y: " + str(positions.y))
            if self.checkPlayPosition(positions.x, positions.y):
                self.selectedCoordinates.append(positions)
                self.repaint()

    def repaint(self):
        if self.SCREEN == 1:
            DRAWER.draw_home()
        elif self.SCREEN == 2:
            DRAWER.draw_grid()
            for coordinate in self.selectedCoordinates:
                #fica piscando... por quanto, desenhando somente circulos
                '''if self.turn:
                    DRAWER.draw_x(coordinate.x, coordinate.y)
                else:
                    DRAWER.draw_circle(coordinate.x, coordinate.y)
                self.turn = not self.turn'''
                DRAWER.draw_circle(coordinate.x, coordinate.y)
        self.update()

    def paintGL(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(5/255, 102/255, 141/255, 1.0)
        # glClearColor(2/255, 195/255, 154/255, 1.0)
        glPointSize(10)

        self.repaint()

