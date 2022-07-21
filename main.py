from itertools import combinations

def inicializa_grafo(grafo):
    arquivo = open("grafo.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.split(" ")
        chave = int(linha[0])
        grafo.update({chave: []})

    for linha in linhas:
        linha = linha.split(" ")
        chave = int(linha[0])

        valor = linha[1].split("\n")
        valor = int(valor[0])
        valor_grafo = grafo.get(chave)

        grafo.update({chave: valor_grafo + [valor]})

    arquivo.close()
    return grafo


#Isso aqui é so pra falar se a solução funciona ou não
def verifica_solucao(grafo, solucao):
    chaves = grafo.keys()
    nao_marcado = chaves - solucao
        
    for k in nao_marcado:
        vizinhos = grafo.get(k)
        # print('vizinho do nao marcado: ', vizinhos)
        for vizinho in vizinhos:
            if vizinho not in solucao:
                # print('nao é solucao')
                return False

    return True


def solucao_otima(grafo):
    tamanho = len(grafo.keys()) 

    solucao_ot = []
    for i in range(tamanho - 1, 0, -1):
        comb = combinations(grafo.keys(), i)
        y = [i for i in comb]
        y = list(map(lambda x: list(x), y))
        # print('\nCombinatoria: ', y)
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


def convert_vertex_to_independent(grafo, solucao):
    return list(grafo.keys() - solucao)


def main():
    grafo = {}
    grafo = inicializa_grafo(grafo)

    solucao = solucao_otima(grafo)
    print('Solução ótima encontrada (Vertex Cover):', solucao)
    
    # conversao = convert_vertex_to_independent(grafo, solucao)
    conversao = convert_vertex_to_independent(grafo, solucao)
    print('\nConversão para Independent Set:', conversao)


main()
