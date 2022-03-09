def numTestes(test):
    while test > 0:
        test -= 1
        palavra1, palavra2 = input().split()
        combinador(palavra1, palavra2)
    return None

def combinador(pala1, pala2):
    palavra = ''
    contadorDeLetras = 0
    while contadorDeLetras < len(pala1) and contadorDeLetras < len(pala2):
        palavra += pala1[contadorDeLetras] + pala2[contadorDeLetras]
        contadorDeLetras += 1
    if contadorDeLetras >= len(pala1):
        palavra += pala2[contadorDeLetras:]
    elif contadorDeLetras >= len(pala2):
        palavra += pala1[contadorDeLetras:]
    return print(palavra)


testes = int(input())
numTestes(testes)