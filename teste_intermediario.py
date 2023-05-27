import sys


def criar_grafo(n_vertices: int) -> list:
    grafo = []

    for i in range(n_vertices):
        linha = [0 for j in range(n_vertices)]
        grafo.append(linha)

    return grafo


def ler_arestas(grafo: list, n_arestas: int) -> None:
    for _ in range(n_arestas):
        v_origem, v_destino, peso = [int(num) for num in input().split()]
        i = v_origem - 1
        j = v_destino - 1

        # grafo não direcionado
        grafo[i][j] = peso
        grafo[j][i] = peso


def dist_min(n_vertices: int, dist: list, visitados: list) -> None:
    min = sys.maxsize

    for u in range(n_vertices):
        if dist[u] < min and visitados[u] == False:
            min = dist[u]
            min_index = u

    return min_index


def dijkstra(grafo: list, n_vertices: int, v_inicial: int) -> list:

    dist = [sys.maxsize] * n_vertices
    dist[v_inicial - 1] = 0
    visitados = [False] * n_vertices
    # armazena quais vértices já foram visitados

    for _ in range(n_vertices):

        # seleciona o vértice com distância mínima dos
        # que ainda não foram processados
        x = dist_min(n_vertices, dist, visitados)

        visitados[x] = True

        # atualiza a menor distância até o vértice y
        # somente se ele não foi visitado e se a nova
        # distância calculada é menor do que a em dist
        for y in range(n_vertices):
            if (
                grafo[x][y] > 0
                and visitados[y] == False
                and (dist[y] > dist[x] + grafo[x][y] or dist[y] == -1)
            ):
                dist[y] = dist[x] + grafo[x][y]

    return dist


def main():
    n_vertices, n_arestas, v_inicial = [int(num) for num in input().split()]

    grafo = criar_grafo(n_vertices)
    ler_arestas(grafo, n_arestas)

    caminhos_minimos = dijkstra(grafo, n_vertices, v_inicial)

    for caminho in caminhos_minimos:
        if caminho == sys.maxsize:
            print(-1)
        else:
            print(caminho)


main()
