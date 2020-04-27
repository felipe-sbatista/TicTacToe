from PySide2.QtWidgets import QLineEdit, QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
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
    turn = 0


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
        self.playBtn = QLabel("Jogar", self)
        self.matrix_game = [[0 for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']

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
            self.playBtn.clear()
            self.playBtn.hide()
            return 2
        return 1

    def checkPlayPosition(self, x, y):
        for coordinate in self.selectedCoordinates:
            if coordinate.x == x and coordinate.y == y:
                print("this field has been already choosen")
                return False
        # self.selectedCoordinates: List[Positions] = []
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
                if self.turn:
                    player = 'O'
                else:
                    player = 'X'

                self.matrix_game[positions.x][positions.y] = player

                if self.hasFinished(positions.x, positions.y):
                    print(player + ' Won!')

    def repaint(self):
        if self.SCREEN == 1:
            self.drawHomeScreen()
        elif self.SCREEN == 2:
            DRAWER.draw_grid()
            for coordinate in self.selectedCoordinates:
                if coordinate.turn == 0:
                    if self.turn:
                        DRAWER.draw_x(coordinate.x, coordinate.y)
                        coordinate.turn = 1
                    else:
                        DRAWER.draw_circle(coordinate.x, coordinate.y)
                        coordinate.turn = 2
                    self.turn = not self.turn
                elif coordinate.turn == 1:
                    DRAWER.draw_x(coordinate.x, coordinate.y)
                    coordinate.turn = 1
                elif coordinate.turn == 2:
                    DRAWER.draw_circle(coordinate.x, coordinate.y)
                    coordinate.turn = 2
                # DRAWER.draw_circle(coordinate.x, coordinate.y)

        self.update()

    def drawHomeScreen(self):
        self.playBtn.setGeometry(282, 215, 80, 50)
        self.playBtn.setStyleSheet("QLabel { background-color : rgb(2, 195, 154);  color: white; font: 25pt; }")
        DRAWER.draw_home()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(5 / 255, 102 / 255, 141 / 255, 1.0)
        # glClearColor(2/255, 195/255, 154/255, 1.0)
        glPointSize(10)
        self.repaint()

    def hasFinished(self, x, y):
        # check if is vertical line
        if (self.matrix_game[0][y] in self.players) and self.matrix_game[0][y] == self.matrix_game[1][y] == \
                self.matrix_game[2][y]:
            return True

        # check if is horizontal line
        if (self.matrix_game[x][0] in self.players) and self.matrix_game[x][0] == self.matrix_game[x][1] == \
                self.matrix_game[x][2]:
            return True

        # check if is in first diagonal
        if (self.matrix_game[0][0] in self.players) and self.matrix_game[0][0] == self.matrix_game[1][1] == \
                self.matrix_game[2][2]:
            return True

        # check if is in second diagonal
        if (self.matrix_game[0][2] in self.players) and self.matrix_game[0][2] == self.matrix_game[1][1] == \
                self.matrix_game[2][0]:
            return True

        return False
