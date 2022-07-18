from itertools import combinations


def inicializa_grafo(grafo):
    arquivo = open("grafo.txt", "r", encoding="utf-8")

    linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.split(" ")
        grafo.update({linha[0]: []})

    for linha in linhas:
        linha = linha.split(" ")
        valor = linha[1].split("\n")
        valor_grafo = grafo.get(linha[0])
        grafo.update({linha[0]: valor_grafo + [valor[0]]})

    arquivo.close()

    return grafo


def verifica_solucao(grafo, solucao):
    chaves = grafo.keys()
    tamanho = len(grafo.keys())
    for i in range(tamanho - 1, 0, -1):
        comb = combinations(grafo.keys(), i)
        y = [i for i in comb]
        y = list(map(lambda x: list(x), y))
        print(y)

        for j in y:
            nao_marcado = chaves - j
            print(list(nao_marcado))
            # verificar se os não_marcados tem seus
            # vizinhos como solução, ou seja, estão marcado


def main():
    grafo = {}
    grafo = inicializa_grafo(grafo)

    solucao = [1, 2]

    verifica_solucao(grafo, solucao)


main()
