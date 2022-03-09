def escrever(valores):
    for item in valores:
        print(item, end=" ")
    print()
    return None


def ler(valores):
    for ind in range(len(valores)):
        valores[ind] = float(input("vs["+str(ind+1)+"] = "))
    return None


def ordenar(valores):
    def ondemenor(vals, inicio):
        posmenor = inicio
        for p in range(inicio+1, len(vals)):
            if vals[p] < vals[posmenor]:
                posmenor = p
        return posmenor
    for ind in range(len(valores)-1):
        posicao = ondemenor(valores, ind)
        temp = valores[ind]
        valores[ind] = valores[posicao]
        valores[posicao] = temp
    return None


TAM = 10
numeros = [0.0]*TAM
ler(numeros)
escrever(numeros)
ordenar(numeros)
escrever(numeros)
