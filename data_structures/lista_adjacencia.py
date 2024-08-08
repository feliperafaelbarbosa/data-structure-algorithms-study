import os

class ListaAdjacencia():
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.grafo = [[] for elemento in range(self.vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.grafo[u - 1].append([v, peso])
        self.grafo[v - 1].append([u, peso])

    def mostrar_vertices(self):
        for i in range(self.vertices):
            print(f'{i + 1}:', end='   ')
            for j in self.grafo[i]:
                print(f'{j} -', end='   ')

            print('')

