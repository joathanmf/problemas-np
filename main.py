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
        print('vizinho do nao marcado: ', vizinhos)
        for vizinho in vizinhos:
            if vizinho not in solucao:
                print('nao é solucao')
                return False
            else:
                print('true')
    return True

def solucao_otima(grafo):
    tamanho = len(grafo.keys()) 

    solucao_ot = []
    for i in range(tamanho - 1, 0, -1):
        comb = combinations(grafo.keys(), i)
        y = [i for i in comb]
        y = list(map(lambda x: list(x), y))
        print('\nCombinatoria: ', y)
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
    
    lista_de_valores_grafo = list(grafo.values())
    valores_grafos = []
    valores_grafos_puros = []
    independet = []
    
    # Colocando as tuplas do grafo em um unico vetor 
    for i in lista_de_valores_grafo:
        valores_grafos = i + valores_grafos
    # Retirando os elementos duplicados
    for element in valores_grafos:
        if element not in valores_grafos_puros:
            valores_grafos_puros.append(element)
    # Por fim, retirando os elementos que contem no vertex e o que sobra 
    # é o independet
    for element in valores_grafos_puros:
        if element not in solucao:
            independet.append(element)
    
    # Falta otimizar o código pois ninguem merece 3 for e muito menos 3 vetor
    return independet
        
def main():
    grafo = {}
    grafo = inicializa_grafo(grafo)

    solucao = solucao_otima(grafo)
    print('\n Solucao otima encontrada: ', solucao)
    
    conversao = convert_vertex_to_independent(grafo, solucao)
    print('\nConversao para Independent Set: ', conversao)

main()
