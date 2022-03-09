def verificacao():
    palavras = []
    frase = input().split()
    while frase != []:
        for palavra in frase:
            if palavra not in palavras:
                palavras.append(palavra)
        frase = input().split()
    return palavras

def printPalavra(pala):
    for palavra1 in pala:
        print(palavra1)


palavras = verificacao()
printPalavra(palavras)