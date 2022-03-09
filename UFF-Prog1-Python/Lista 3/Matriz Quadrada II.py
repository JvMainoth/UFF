def entradas ():
    entradas = int(input())
    while entradas != 0:
        montarMatriz(entradas)
        entradas = int(input())
    return

def montarMatriz(ent):
    matriz = []
    for i in range(1,(ent + 1)):
        matrizTemp = []
        cont = i
        for i2 in range(ent):
            matrizTemp.append(abs(cont))
            if cont == 1:
                cont -= 3
            else:
                cont -= 1
        matriz.append(matrizTemp)
    for i3 in range(ent):
        texto = ''
        for i4 in range(ent):
            texto += " %3d" % matriz[i3][i4]
        print(texto[1:])
    print('')
    return

entradas()