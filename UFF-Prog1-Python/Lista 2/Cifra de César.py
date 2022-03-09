def numTeste(teste):
    while teste > 0:
        decodificacao(teste)
        teste -= 1
    return None


def decodificacao(t):
    for i in range(t):
        texto = input()
        movLetra = int(input())
        nova_letra = ''
        for l in texto:
            posicao = ord(l) - movLetra
            if posicao < 65:
                nova_letra += chr(91 - (65 - posicao))
            else:
                nova_letra += chr(ord(l) - movLetra)
        return print(nova_letra)


testes = int(input())
numTeste(testes)
