def numTeste(teste):
    while teste > 0:
        reversao(teste)
        teste -= 1
    return None

def reversao(testa):
    frase = input()
    reforma = int(len(frase) / 2) - 1
    correcao = frase[reforma::-1] + frase[len(frase) - 1:reforma:-1]
    return print(correcao)


testes = int(input())
numTeste(testes)