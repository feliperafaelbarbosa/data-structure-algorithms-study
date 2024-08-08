import os

class MatrizAdjacencia():
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for elemento in range(self.vertices)]

    # Para grafos simétricos
    def adicionar_aresta(self, u, v, peso) -> None:
        self.grafo[u - 1][v - 1] += 1
        self.grafo[v - 1][u - 1] += 1

    # Para grafos não-simétricos
    # def adicionar_arco(self, u, v, peso) -> None:
    #     self.grafo[u - 1][v - 1] += peso

    def visualizar_matriz_de_adjacencia(self) -> None:
        for elemento in range(self.vertices):
            print(f'{self.grafo[elemento]}')

