from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Inputs
        self.alturaBox = QtWidgets.QComboBox(self.centralwidget)
        self.alturaBox.setGeometry(QtCore.QRect(10, 70, 171, 32))
        self.alturaBox.setObjectName("alturaBox")
        self.labelAltura = QtWidgets.QLabel(self.centralwidget)
        self.labelAltura.setGeometry(QtCore.QRect(10, 50, 58, 18))
        self.labelAltura.setObjectName("labelAltura")

        self.pesoBox = QtWidgets.QComboBox(self.centralwidget)
        self.pesoBox.setGeometry(QtCore.QRect(10, 190, 171, 32))
        self.pesoBox.setObjectName("pesoBox")
        self.labelPeso = QtWidgets.QLabel(self.centralwidget)
        self.labelPeso.setGeometry(QtCore.QRect(10, 170, 91, 18))
        self.labelPeso.setObjectName("labelPeso")

        self.velocidadeBox = QtWidgets.QComboBox(self.centralwidget)
        self.velocidadeBox.setGeometry(QtCore.QRect(10, 130, 171, 32))
        self.velocidadeBox.setObjectName("velocidadeBox")
        self.labelVelocidade = QtWidgets.QLabel(self.centralwidget)
        self.labelVelocidade.setGeometry(QtCore.QRect(10, 110, 71, 18))
        self.labelVelocidade.setObjectName("labelVelocidade")


        self.arremessoBox = QtWidgets.QComboBox(self.centralwidget)
        self.arremessoBox.setGeometry(QtCore.QRect(10, 250, 171, 32))
        self.arremessoBox.setObjectName("arremessoBox")
        self.labelArremesso = QtWidgets.QLabel(self.centralwidget)
        self.labelArremesso.setGeometry(QtCore.QRect(10, 230, 161, 18))
        self.labelArremesso.setObjectName("labelArremesso")

        self.assistenciaBox = QtWidgets.QComboBox(self.centralwidget)
        self.assistenciaBox.setGeometry(QtCore.QRect(10, 300, 171, 32))
        self.assistenciaBox.setObjectName("assistenciaBox")
        self.labelAssistencia = QtWidgets.QLabel(self.centralwidget)
        self.labelAssistencia.setGeometry(QtCore.QRect(10, 280, 161, 18))
        self.labelAssistencia.setObjectName("labelAssistencia")

        self.enterradaBox = QtWidgets.QComboBox(self.centralwidget)
        self.enterradaBox.setGeometry(QtCore.QRect(10, 350, 171, 32))
        self.enterradaBox.setObjectName("enterradaBox")
        self.labelEnterrada = QtWidgets.QLabel(self.centralwidget)
        self.labelEnterrada.setGeometry(QtCore.QRect(10, 330, 161, 18))
        self.labelEnterrada.setObjectName("labelEnterrada")

        # Botões
        self.treinoButton = QtWidgets.QPushButton(self.centralwidget)
        self.treinoButton.setGeometry(QtCore.QRect(10, 10, 171, 34))
        self.treinoButton.setObjectName("treinoButton")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(10, 400, 171, 34))
        self.pushButton.setObjectName("pushButton")

        
        # Input Saída
        self.outputText = QtWidgets.QTextEdit(self.centralwidget)
        self.outputText.setEnabled(False)
        self.outputText.setGeometry(QtCore.QRect(190, 90, 421, 351))
        self.outputText.setObjectName("outputText")

        # Parâmetros
        self.neuroEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.neuroEdit.setGeometry(QtCore.QRect(340, 10, 31, 32))
        self.neuroEdit.setObjectName("neuroEdit")
        self.labelNeuronios = QtWidgets.QLabel(self.centralwidget)
        self.labelNeuronios.setGeometry(QtCore.QRect(270, 20, 81, 18))
        self.labelNeuronios.setObjectName("labelNeuronios")

        self.labelCamadas = QtWidgets.QLabel(self.centralwidget)
        self.labelCamadas.setGeometry(QtCore.QRect(205, 60, 151, 18))
        self.labelCamadas.setObjectName("labelCamadas")
        self.camadasEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.camadasEdit.setGeometry(QtCore.QRect(340, 50, 31, 32))
        self.camadasEdit.setObjectName("camadasEdit")

        self.labelAlteracoes = QtWidgets.QLabel(self.centralwidget)
        self.labelAlteracoes.setGeometry(QtCore.QRect(390, 20, 121, 18))
        self.labelAlteracoes.setObjectName("labelAlteracoes")

        self.iterEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.iterEdit.setGeometry(QtCore.QRect(520, 10, 91, 32))
        self.iterEdit.setObjectName("iterEdit")

        self.labelAprendTx = QtWidgets.QLabel(self.centralwidget)
        self.labelAprendTx.setGeometry(QtCore.QRect(380, 60, 141, 18))
        self.labelAprendTx.setObjectName("labelAprendTx")

        self.aprendEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.aprendEdit.setGeometry(QtCore.QRect(520, 50, 91, 32))
        self.aprendEdit.setObjectName("aprendEdit")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "NBAPlayerPosition"))

        self.treinoButton.setText(_translate("MainWindow", "Treinar"))
        self.pushButton.setText(_translate("MainWindow", "Reconhecer"))

        self.labelAltura.setText(_translate("MainWindow", "Altura:"))
        self.labelPeso.setText(_translate("MainWindow", "Peso:"))
        self.labelVelocidade.setText(_translate("MainWindow", "Velocidade:"))
        self.labelArremesso.setText(_translate("MainWindow", "Arremesso:"))
        self.labelAssistencia.setText(_translate("MainWindow", "Assistência:"))
        self.labelEnterrada.setText(_translate("MainWindow", "Enterrada:"))


        self.neuroEdit.setText(_translate("MainWindow", "8"))
        self.labelNeuronios.setText(_translate("MainWindow", "Camadas:"))

        self.labelCamadas.setText(_translate("MainWindow", "Neurônios por Camada:"))
        self.camadasEdit.setText(_translate("MainWindow", "8"))

        self.labelAlteracoes.setText(_translate("MainWindow", "Iterações máximas:"))
        self.iterEdit.setText(_translate("MainWindow", "20000"))

        self.labelAprendTx.setText(_translate("MainWindow", "Taxa de aprendizado:"))
        self.aprendEdit.setText(_translate("MainWindow", "0.001"))