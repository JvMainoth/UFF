def produz(tMin, tMax, nm):
    dicionarioPal = {}
    dados = open(nm, "r", encoding="utf-8")
    valorLinha = 1
    for linha in dados:
        palavras = linha.strip('\n').split()
        for p in palavras:
            if p in dicionarioPal:
                dicionarioPal[p].add(valorLinha)
            elif tMin <= len(p) <= tMax:
                dicionarioPal[p] = set()
                dicionarioPal[p].add(valorLinha)
        valorLinha += 1
    dados.close()
    return dicionarioPal

def formatacao(dictPal):
    for i in sorted(dictPal.keys()):
        print("Chave: %s" % i)
        print("Linha em que ocorre:")
        for i2 in dictPal[i]:
            print('\t%s' % i2)



nome = input()
tamMin, tamMax = map(int, input().split())
dicionarioPalavras = produz(tamMin, tamMax, nome)
formatacao(dicionarioPalavras)
