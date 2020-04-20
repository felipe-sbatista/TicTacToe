from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QOpenGLWidget

from game import Game
from game_window import GameWindow

if __name__ == "__main__":
    app = QApplication([])
    opengl_widget = QOpenGLWidget()
    opengl_widget.setFocusPolicy(Qt.StrongFocus)
    game_widget = Game(opengl_widget)
    main_window = GameWindow(game_widget)
    exit(app.exec_())

