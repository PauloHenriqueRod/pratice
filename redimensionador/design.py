# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redimensionador.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.aqui_largura = QtWidgets.QLineEdit(self.centralwidget)
        self.aqui_largura.setObjectName("aqui_largura")
        self.gridLayout.addWidget(self.aqui_largura, 2, 1, 1, 1)
        self.largura = QtWidgets.QLabel(self.centralwidget)
        self.largura.setObjectName("largura")
        self.gridLayout.addWidget(self.largura, 2, 0, 1, 1)
        self.aqui_altura = QtWidgets.QLineEdit(self.centralwidget)
        self.aqui_altura.setObjectName("aqui_altura")
        self.gridLayout.addWidget(self.aqui_altura, 2, 3, 1, 1)
        self.altura = QtWidgets.QLabel(self.centralwidget)
        self.altura.setObjectName("altura")
        self.gridLayout.addWidget(self.altura, 2, 2, 1, 1)
        self.area = QtWidgets.QScrollArea(self.centralwidget)
        self.area.setWidgetResizable(True)
        self.area.setObjectName("area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 483, 366))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.area, 0, 0, 1, 5)
        self.botao_redimensionar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_redimensionar.setObjectName("botao_redimensionar")
        self.gridLayout.addWidget(self.botao_redimensionar, 2, 4, 1, 1)
        self.botao_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName("botao_salvar")
        self.gridLayout.addWidget(self.botao_salvar, 3, 4, 1, 1)
        self.escolhe = QtWidgets.QPushButton(self.centralwidget)
        self.escolhe.setObjectName("escolhe")
        self.gridLayout.addWidget(self.escolhe, 1, 4, 1, 1)
        self.abre_arquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.abre_arquivo.setObjectName("abre_arquivo")
        self.gridLayout.addWidget(self.abre_arquivo, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "redimensionador de arquivo"))
        self.largura.setText(_translate("MainWindow", "LARGURA"))
        self.altura.setText(_translate("MainWindow", "ALTURA"))
        self.label.setText(_translate("MainWindow", "imagem"))
        self.botao_redimensionar.setText(_translate("MainWindow", "REDIMENSIONAR"))
        self.botao_salvar.setText(_translate("MainWindow", "SALVAR"))
        self.escolhe.setText(_translate("MainWindow", "escolher arquivo"))
