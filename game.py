from PySide2.QtWidgets import QHBoxLayout, QWidget, QApplication, QVBoxLayout,  QPushButton, QLabel, QMainWindow, QOpenGLWidget, QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *
from OpenGL.GL import *
import env
import drawer


class Game(QOpenGLWidget):

    def initializeGL(self):
        self.setFixedSize(QSize(env.VIEW_WIDTH, env.VIEW_HEIGHT))
        glViewport(0, 0, env.VIEW_WIDTH, env.VIEW_HEIGHT)

    def paintGL(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.59, 0.67, 0.60, 1.0)
        glPointSize(10)

        glBegin(GL_POINTS)

        glColor3f(0.9, 0.2, 0.15) # apples
        # draw_apples()

        # glColor3f(0.0, 0.0, 0.0) # snake
        # draw_snake()

        glEnd()
