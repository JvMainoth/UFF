#Programa
#SubPrograma
def produz(nm):
    dicionarioPsOcs = dict()  # ou {}
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        palavras = linha.strip("\n").split()
        for p in palavras:
            if p not in dicionarioPsOcs: # oudicionarioPsOcs.get(p) == None:
                dicionarioPsOcs[p] = 1
            else:
                dicionarioPsOcs[p] += 1
    dados.close()
    return dicionarioPsOcs

def mostrar(dicionarioPsOcs):
    print("Conteúdo do Dicionário:")
    for chave, valor in sorted(dicionarioPsOcs.items()):
        print("\t%13s %2d" % (chave+" "*(13-len(chave)), valor))
    print()
    return None
#Principal
nome = input()
dicionarioPalavrasOcorrencias = produz(nome)
mostrar(dicionarioPalavrasOcorrencias)