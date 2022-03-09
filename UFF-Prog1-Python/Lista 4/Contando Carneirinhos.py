def numTestes(test):
    while test > 0:
        test -= 1
        num = int(input())
        carneiros(num)
    return None


def carneiros(numCarneiros):
    valores = list(map(int, input().split()))
    listaUnica = []
    cont = 0
    for i in valores:
        listaUnica.append(i)
    return print(len(set(listaUnica)))


testes = int(input())
numTestes(testes)