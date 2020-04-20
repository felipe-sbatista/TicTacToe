from PySide2.QtWidgets import QWidget, QVBoxLayout

import colors
import env


class GameWindow(QWidget):
    def __init__(self, game_widget):
        super(GameWindow, self).__init__()

        self.game_widget = game_widget
        self.setFixedSize(env.VIEW_WIDTH + 40, env.VIEW_HEIGHT + 20)
        self.setStyleSheet(colors.BACKGROUND_COLOR)
        self.autoFillBackground()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.game_widget)
        self.setLayout(layout)
        self.show()
