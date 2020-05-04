import PySide2
from PySide2.QtWidgets import QLineEdit, QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QMainWindow, \
    QOpenGLWidget, QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *
from OpenGL.GL import *
import env
from drawer import Drawer
from typing import List

DRAWER = Drawer()


class Positions:
    x = 0
    y = 0
    turn = 0


class Game(QOpenGLWidget):
    selectedCoordinates: List[Positions] = []
    SCREEN = 1
    gameTitle = None
    playButtonLabel = None
    def __init__(self, QOpenGLWidget):
        super().__init__()
        '''
        if turn equals to false, then cirlcle will be marked
        and if its equals to true, then X will be marked 
        '''
        self.turn = False
        self.initializeHomeScreen()
        self.matrix_game = [[0 for _ in range(3)] for _ in range(3)]
        self.players = ['X', 'O']

    def initializeGL(self):
        self.resize(env.VIEW_WIDTH, env.VIEW_HEIGHT)
        glViewport(0, 0, env.VIEW_WIDTH, env.VIEW_HEIGHT)

    def resizeEvent(self, e: PySide2.QtGui.QResizeEvent):
        super().resizeEvent(e)
        width = self.SCREEN == 1 and 220 or 400
        if self.gameTitle is not None:
            x = e.size().width() / 3
            y = e.size().height() / 2
            self.gameTitle.setGeometry(int(x), int(y)-100, width, 50)

        if self.playButtonLabel is not None:
            x = e.size().width() / 3
            y = e.size().height() / 3
            self.playButtonLabel.setGeometry(int(x), int(y)+50, width, 50)

    def initializeHomeScreen(self):
        self.gameTitle = QLabel("Tic Tac Toe", self)
        self.playButtonLabel = QLabel("Jogar", self)
        self.gameTitle.setStyleSheet(env.titleLabelProps)
        self.playButtonLabel.setStyleSheet(env.btnLabelProps)

    def initializeEndScreen(self, victoryMsg):
        self.gameTitle = QLabel(victoryMsg, self)
        self.playButtonLabel = QLabel("Jogar Novamente", self)
        self.gameTitle.setStyleSheet(env.titleLabelProps)
        self.playButtonLabel.setStyleSheet(env.btnLabelProps)
        print(self.geometry().x(), self.geometry().y())
        self.gameTitle.setGeometry(int(self.geometry().x()*9), int(self.geometry().y()*9) - 100, 420, 50)
        self.playButtonLabel.setGeometry(int(self.geometry().x()*9), int(self.geometry().y()*10) + 50, 400, 50)

    def calculateCoordinates(self, x, y):
        coordinates = Positions()
        # get width and height in case of resizes
        # divides by 3 due to 9x9 matrix of tic tac toe
        w1 = self.geometry().width()/3
        w2 = w1 * 2
        h1 = self.geometry().height()/3
        h2 = h1 * 2

        # identifying x index
        if 0 <= x < w1:
            coordinates.x = 0
        elif w1 <= x < w2:
            coordinates.x = 1
        else:
            coordinates.x = 2

        # identifying y index
        if 0 <= y < h1:
            coordinates.y = 0
        elif h1 <= y < h2:
            coordinates.y = 1
        else:
            coordinates.y = 2

        return coordinates

    def switchButtonsState(self, activate):
        if activate:
            self.playButtonLabel.show()
            self.gameTitle.show()
        else:
            self.playButtonLabel.hide()
            self.gameTitle.hide()

    def calculateCoordinatesHome(self, x, y):
        print(x, y, 215 <= x < 426, 204 <= y < 280)
        btnGeometry = self.playButtonLabel.geometry()
        print(self.playButtonLabel.geometry().x(), self.playButtonLabel.geometry().width())
        if btnGeometry.x() <= x < btnGeometry.x() + btnGeometry.width() and btnGeometry.y() <= y < btnGeometry.y() + btnGeometry.height():
            self.switchButtonsState(False)
            return 2
        return 1

    def clearBoard(self):
        self.selectedCoordinates: List[Positions] = []
        self.matrix_game = [[0 for _ in range(3)] for _ in range(3)]

    def checkPlayPosition(self, x, y):
        for coordinate in self.selectedCoordinates:
            if coordinate.x == x and coordinate.y == y:
                print("Esse campo já foi escolhido")
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
                if self.turn:
                    player = 'O'
                else:
                    player = 'X'

                self.matrix_game[positions.x][positions.y] = player

                if self.hasFinished(positions.x, positions.y):
                    self.initializeEndScreen("O Jogador '" + player + "' Ganhou!")
                    print(player + ' Won!')
                    self.clearBoard()
                    self.SCREEN = 1
                    self.repaint()
                else:
                    draw = True
                    for line in range(3):
                        for column in range(3):
                            if self.matrix_game[line][column] != 'X' and self.matrix_game[line][column] != 'O':
                                draw = False
                    if draw:
                        self.initializeEndScreen("Deu velha")
                        print('Deu velha')
                        self.clearBoard()
                        self.SCREEN = 1
                        self.repaint()

    def repaint(self):
        if self.SCREEN == 1:
            self.switchButtonsState(True)

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
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(5 / 255, 102 / 255, 141 / 255, 1.0)
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
