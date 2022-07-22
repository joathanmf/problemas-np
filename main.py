from itertools import combinations
import json


def inicializa_grafo(grafo):
    with open("grafo.json", "r") as fp:
        grafo = json.load(fp,
                          object_hook=lambda d:
                          {int(k) if k else k: v
                           for k, v in d.items()})

    return grafo


#Isso aqui é so pra falar se a solução funciona ou não
def verifica_solucao(grafo, solucao):
    chaves = grafo.keys()
    nao_marcado = chaves - solucao

    for k in nao_marcado:
        vizinhos = grafo.get(k)
        for vizinho in vizinhos:
            if vizinho not in solucao:
                return False

    return True


def solucao_otima(grafo):
    tamanho = len(grafo.keys())

    solucao_ot = []
    for i in range(tamanho - 1, 0, -1):
        comb = combinations(grafo.keys(), i)
        y = [i for i in comb]
        y = list(map(lambda x: list(x), y))

        for combinatoria in y:
            ehSolucao = verifica_solucao(grafo, combinatoria)
            # Se a combinatoria de tamanho i é uma solucao, entao achamos uma solucao de tamanho i
            # Entao podemos começar verificar as combinatorias de tamanho i - 1
            if ehSolucao:
                solucao_ot = combinatoria
                break
        # Se foi achado uma solucao de tamanho i entao podemos continuar verificando
        # Se nao, a solucao otima tem tamanho i + 1, logo diferente de i, entao retorna a solucao otima
        if len(solucao_ot) != i:
            return solucao_ot


def solucao_k(grafo, k):
    k2 = k
    k = len(grafo.keys()) - k

    if k <= len(grafo.keys()) and k >= 0 and k2 > 0:
        solucao_ot = []
        comb = combinations(grafo.keys(), k)
        y = [k for k in comb]
        y = list(map(lambda x: list(x), y))

        for combinatoria in y:
            ehSolucao = verifica_solucao(grafo, combinatoria)
            if ehSolucao:
                solucao_ot = combinatoria
                break

        if solucao_ot != []:
            indep_set = convert_vertex_to_independent(grafo, solucao_ot)
            print(f"Solução: {indep_set}")
            return True
    else:
        print("O valor do k está incorreto.")

    return False


def convert_vertex_to_independent(grafo, solucao):
    return list(grafo.keys() - solucao)


def main():
    grafo = {}
    grafo = inicializa_grafo(grafo)

    # -------------------- Etapa 1
    print("\n# ---------- Etapa 1 ---------- #\n")

    possivel_solucao = [0, 2, 4]
    print(f"Possível solução para o Vertex Cover: {possivel_solucao}")

    if verifica_solucao(grafo, possivel_solucao):
        print("Sim, é uma solução.\n")
    else:
        print("Não, essa não é uma solução.\n")

    # -------------------- Etapa 2
    print("# ---------- Etapa 2 ---------- #\n")

    solucao = solucao_otima(grafo)
    print(f"Solução ótima para o Vertex Cover: {solucao}")

    conversao = convert_vertex_to_independent(grafo, solucao)
    print(f"Conversão para Independent Set: {conversao}")

    print("\n# ---------- ------- ---------- #\n")

    k = 2
    sol_k = solucao_k(grafo, k)

    if sol_k:
        print(f"Há solução para o Independent Set com k = {k}.")
    else:
        print(f"Não há solução para o k = {k}.")

    print("\n# ---------- ------- ---------- #\n")


main()
