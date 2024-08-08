from data_structures.matriz_adjacencia import MatrizAdjacencia
from data_structures.lista_adjacencia import ListaAdjacencia

if __name__ == '__main__':
    ma = MatrizAdjacencia(4)
    ma.adicionar_aresta(2, 3, 10)
    ma.visualizar_matriz_de_adjacencia()


    la = ListaAdjacencia(4)
    la.adicionar_aresta(1, 2, 10)
    la.adicionar_aresta(1, 3, 30)
    la.adicionar_aresta(1, 4, 100)

    la.adicionar_aresta(2, 1, 10)
    la.adicionar_aresta(2, 3, 20)

    la.adicionar_aresta(3, 1, 50)

    la.mostrar_vertices()