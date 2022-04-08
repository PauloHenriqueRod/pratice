import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Arquivo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.escolhe.clicked.connect(self.abrir_imagem())

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'escolher arquivo',
            r'C:\Users\Paulo\OneDrive\Imagens'
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    arquivo = Arquivo()
    arquivo.show()
    qt.exec_()
