#!/usr/bin/python3

# Importa MLPClassifier (classificador Multi Layer Perceptron)
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import Normalizer

# Instancia a rede neural
def cria_rede(camadas, neuronios_por_camada, iteracoes, aprend):
    return MLPClassifier(hidden_layer_sizes=(neuronios_por_camada,)*camadas, max_iter=iteracoes, learning_rate_init=aprend, tol=1e-4)

def treina_rede(rede):

    X = [[0,	0,0,	1,1,	1,1,	1,1,	0,0],    #S. Curry
         [0,	0,0,	1,1,	1,1,	1,1,	0,0],    # T. Young
         [1,	1,0,	0,1,	1,1,	1,1,	0,1],    # L. Doncic
         [0,	0,0,	1,1,	1,0,	1,1,	1,1],    # J. Morant
         [0,	0,0,	1,0,	1,0,	1,1,	0,0],    # C. Paul
         [0,	0,0,	1,1,	1,1,	1,1,	0,0],    # K. Irving
         [1,	0,1,	1,0,	1,1,	1,1,	1,0],    # J. Harden

         [1,	1,1,	1,1,	1,0,	1,1,	1,1],    # L. James
         [1,	0,1,	1,0,	1,0,	1,0,	1,0],    # D. Booker
         [1,	0,1,	1,0,	1,0,	1,0,	1,0],    # P. George
         [1,	1,0,	0,1,	0,1,	1,0,	1,0],    # K. Leonard
         [1,	1,1,	1,1,	0,1,	1,0,	1,1],    # G. Antetokounmpo
         [1,	1,0,	1,0,	1,1,	1,0,	1,0],    # K. Durant
         [1,	0,1,	1,0,	1,1,	0,1,	1,0],    # K. Thompson

         [1,	1,1,	0,0,	0,1,	1,1,	1,1],    # N. Jokic
         [1,	1,1,	0,1,	0,1,	1,0,	1,1],    # J. Embiid
         [1,	1,1,	0,1,	0,0,	0,1,	1,0],    # B. Adebayo
         [1,	1,1,	0,0,	0,0,	0,0,	1,1],    # R. Gobert
         [1,	1,0,	0,0,	0,0,	0,1,	1,0],    # J. Allen
         [1,	1,1,	0,0,	0,0,	0,1,	1,1],    # D. Ayton
         [1,	0,1,	0,0,	0,1,	0,0,	1,1]]   # C. Wood

    # Resultados previstos
    y = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],
         [0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],
         [1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0]] 

    # Treina a rede neural
    rede.fit(X, y)

    
# Testa a rede neural
def testa_rede(rede, entrada):
    pred = rede.predict([entrada])
    return pred