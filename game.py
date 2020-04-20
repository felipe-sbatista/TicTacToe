from PySide2.QtWidgets import QHBoxLayout, QWidget, QApplication, QVBoxLayout,  QPushButton, QLabel, QMainWindow, QOpenGLWidget, QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *
from OpenGL.GL import *
import env
from drawer import Drawer


class Game(QOpenGLWidget):

    def initializeGL(self):
        self.setFixedSize(QSize(env.VIEW_WIDTH, env.VIEW_HEIGHT))
        glViewport(0, 0, env.VIEW_WIDTH, env.VIEW_HEIGHT)

    def paintGL(self):

        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(1, 0.67, 0.30, 1.0)
        glPointSize(10)

        drawer = Drawer()
        drawer.draw_grid()
        drawer.draw_circle(0)

