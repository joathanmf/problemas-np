from itertools import combinations as comb


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


def combinatoria(grafo):
    comb(grafo.keys())


def verifica_solucao(grafo, solucao):
    pass


def main():
    grafo = {}
    grafo = inicializa_grafo(grafo)
    # print(grafo.keys())

    # solucao = [1, 2]

    # verifica_solucao(grafo, solucao)


main()
