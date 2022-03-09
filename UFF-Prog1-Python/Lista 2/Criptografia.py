#SubPrograma


def numTeste(teste):
    while teste > 0:
        criptografia1(teste)
        teste -= 1
    return None


def criptografia1(teste):
    from math import ceil
    for t in range(teste):
        palavra = input()
        novaPalavra = ''
        for i in palavra:
            if (i.isalpha() == True):
                novaPalavra += chr(ord(i) + 3)
            else:
                novaPalavra += i
        novaPalavra2 = novaPalavra[::-1]
        s = ceil(len(novaPalavra2)/2)
        novaPalavra3 = novaPalavra2[-s:]
        novaPalavra4 = ''
        for v in novaPalavra3:
            novaPalavra4 += chr(ord(v) - 1)
        palavrafinal = novaPalavra2.replace(novaPalavra3, novaPalavra4)
        return print(palavrafinal)


#Programa Principal
testes = int(input())
numTeste(testes)
