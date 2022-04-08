import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

caminho = 'C:/Users/Paulo/OneDrive/Imagens'
caminho_final = 'C:/Users/Paulo/OneDrive/Área de Trabalho'


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.escolhe.clicked.connect(self.abrir_imagem)
        self.botao_redimensionar.clicked.connect(self.redimensionar)
        self.botao_salvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            f'{caminho}',
            options=QFileDialog.DontUseNativeDialog
        )
        self.abre_arquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.label.setPixmap(self.original_img)
        self.aqui_largura.setText(str(self.original_img.width()))
        self.aqui_largura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.aqui_largura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.label.setPixmap(self.nova_imagem)
        self.aqui_largura.setText(str(self.nova_imagem.width()))
        self.aqui_altura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            f'{caminho_final}',
            options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
