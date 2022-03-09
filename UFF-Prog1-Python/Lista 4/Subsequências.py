def numTestes(test):
    while test > 0:
        test -= 1
        sequencia = input()
        subsequencia(sequencia)
    return None


def subsequencia(sequencia):
    teste = int(input())
    while teste > 0:
        teste -= 1
        fragmento = list(input())
        palavra = list(sequencia)
        for i in range(len(fragmento)):
            for i2 in range(len(palavra)):
                if fragmento[i] == palavra[i2]:
                    fragmento[i] = fragmento[i].upper()
                    palavra[i2] = palavra[i2].upper()
                    del(palavra[:i2])


















    return None


testes = int(input())
numTestes(testes)