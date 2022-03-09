def numTestes(test):
    while test > 0:
        test -= 1
        num = int(input())
        comandos(num)
    return None

def comandos(n):
    cont = 0
    lista = []
    for i in range(0, n):
        lista.append(input())
    for i2 in range(0, n):
        if lista[i2] == "LEFT":
            cont -= 1
        elif lista[i2] == "RIGHT":
            cont += 1
        else:
            lista[i2] = lista[i2].split()
            lista[i2] = lista[i2][len(lista[i2])-1]
            lista[i2] = lista[int(lista[i2])-1]
            if lista[i2] == 'LEFT':
                cont -= 1
            else:
                cont += 1
    print(cont)

testes = int(input())
numTestes(testes)