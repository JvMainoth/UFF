def numTestes(test):
    while test > 0:
        test -= 1
        codigin = input().split()
        ordenador(codigin)
        print()
    return None

def ordenador(cod):
    cod.sort(key=len, reverse=True)
    for i in range(len(cod)):
        print(cod[i], end='')
        if i != len(cod) - 1:
            print(' ', end='')


testes = int(input())
numTestes(testes)