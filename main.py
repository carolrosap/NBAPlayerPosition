#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import ui
import rede_neural

class MainWindow(QMainWindow, ui.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.treinoButton.clicked.connect(self.botao_treino)
        self.pushButton.clicked.connect(self.botao_push)
        self.alturaBox.addItems(["< 195cm", ">= 195cm"])
        self.pesoBox.addItems(["< 90kg", "90 - 100kg", "100 - 110kg", "> 110kg"])
        self.velocidadeBox.addItems(["Muito lento", "Lento", "Rápido", "Muito rápido"])
        self.arremessoBox.addItems(["Ruim", "Mediano", "Bom", "Excelente"])
        self.assistenciaBox.addItems(["Ruim", "Mediano", "Bom", "Excelente"])
        self.enterradaBox.addItems(["Ruim", "Mediano", "Bom", "Excelente"])

        self.rede = None

    def botao_treino(self):
        self.rede = rede_neural.cria_rede(int(self.neuroEdit.text()), int(self.camadasEdit.text()), int(self.iterEdit.text()), float(self.aprendEdit.text()))
        rede_neural.treina_rede(self.rede)
        self.pushButton.setEnabled(True)

        params = self.rede.get_params()
        self.RNA_Attributes =    f"Erro atingido no aprendizado: {self.rede.loss_}"\
                            f"\nMenor erro: {self.rede.best_loss_}"\
                            f"\nNúmero de iterações atingido no aprendizado: {self.rede.n_iter_}"\
                            f"\nTaxa de aprendizado: {params['learning_rate_init']}"\
                            f"\nNúmero de camadas: {self.rede.n_layers_}"\
                            f"\nNeurônios das camadas intermediárias: {params['hidden_layer_sizes']}"\

        print(f"Pesos: {self.rede.coefs_}")

        self.outputText.setText(self.RNA_Attributes)

    def botao_push(self):
        entrada = ""
        entrada += "{0:b}".format(self.alturaBox.currentIndex())
        entrada += "{0:02b}".format(self.pesoBox.currentIndex())
        entrada += "{0:02b}".format(self.velocidadeBox.currentIndex())
        entrada += "{0:02b}".format(self.arremessoBox.currentIndex())  
        entrada += "{0:02b}".format(self.assistenciaBox.currentIndex())
        entrada += "{0:02b}".format(self.enterradaBox.currentIndex())
        entrada_preparada = list(map(int, list(entrada)))

        saida = rede_neural.testa_rede(self.rede, entrada_preparada)
        saida_preparada = "".join([str(s) for s in saida[0]])

        subgeneros = {"00": "Posição: Armador\nValores do padrão de saída reconhecido: (0, 0)",
                      "01": "Posição: Ala\nValores do padrão de saída reconhecido: (0, 1)",
                      "10": "Posição: Pivô\nValores do padrão de saída reconhecido: (1, 0)"}

        saida_preparada =   f"{self.RNA_Attributes}" \
                            f"\n\nValores dos padrões de entrada: {entrada_preparada}" \
                            f"\n{subgeneros[saida_preparada]}"

        print(entrada_preparada)
        self.outputText.setText(saida_preparada)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()