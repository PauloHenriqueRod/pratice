import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout
import pygame


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('APERTE AQUI')
        self.btn.setStyleSheet('font-size: 40px:;')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('musica.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
