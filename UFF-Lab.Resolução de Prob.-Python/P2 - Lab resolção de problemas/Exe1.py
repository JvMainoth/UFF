def numTestes(test):
    while test > 0:
        test -= 1
        frase = input()
        senha(frase)
    return None

def senha(fra):
    frase_nova = fra.split()
    letra = ''
    for i in range(len(frase_nova)):
        letra += frase_nova[i][0]
    print(letra)
    return None


testes = int(input())
numTestes(testes)