arquivo = open("grafo")
grafo = {}

linhas = arquivo.readlines()

for linha in linhas:
    linha = linha.split(" ")
    grafo.update({linha[0]: []})

for linha in linhas:
    linha = linha.split(" ")
    valor = linha[1].split("\n")
    valor_grafo = grafo.get(linha[0])
    grafo.update({linha[0]: valor_grafo + [valor[0]]})

# print(valor_grafo)

# print(grafo.items())
