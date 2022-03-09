#Subprograma
def mostra(conjPals, nm):
    print("Conteúdo do Conjunto de palavras no Arquivo", nm+":")
    if len(conjPals) == 0:
        print("\t Conjunto Vazio!!!")
    else:
        for palavra in conjPals:
            print("\t", palavra)
    print()
    return None

def produz(nm, dPalsOcs):
    conjPals = set()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        palavras = linha.strip().split()
        for p in palavras:
            conjPals.add(p)
            if p not in dPalsOcs:
                dPalsOcs[p] = 1
            else:
                dPalsOcs[p] += 1
    dados.close()
    return conjPals


def achaModa(dPalsOcs):
    if len(dPalsOcs) == 0:
        return None
    else:
        palavraMaisFrequente = None
        for palavra in dPalsOcs:
            if palavraMaisFrequente == None:
                palavraMaisFrequente = palavra
            elif dPalsOcs[palavra] > dPalsOcs[palavraMaisFrequente]:
                palavraMaisFrequente = palavra
        return palavraMaisFrequente
#Programa Principal
dPalavrasOcorrencias = dict()
nomeArq = input()
while nomeArq != "":
    conjPalavrasNoArquivo = produz(nomeArq, dPalavrasOcorrencias)
    mostra(conjPalavrasNoArquivo, nomeArq)
    moda = achaModa(dPalavrasOcorrencias)
    print("Palavra Mais Frequente até este arquivo:", moda)
    nomeArq = input()