from PySide2.QtWidgets import QWidget, QVBoxLayout

import env


class GameWindow(QWidget):
    def __init__(self, game_widget):
        super(GameWindow, self).__init__()

        self.game_widget = game_widget


        hor_border: int = int(20)
        ver_border: int = int(40)

        self.setFixedSize(env.VIEW_WIDTH + hor_border, env.VIEW_HEIGHT + ver_border)
        self.setStyleSheet('background-color: #222222')
        self.autoFillBackground()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.game_widget)
        self.setLayout(layout)
        self.show()
