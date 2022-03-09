def montarVetor():
    valores = [0] * 20
    for i in range(len(valores)):
        valores[i] = int(input())
    return valores

def trocaVetores(vet):
    cont = 19
    for i in range(len(vet)):
        if i <= 9:
            numTemp = vet[i]
            vet[i] = vet[cont]
            vet[cont] = numTemp
            cont -= 1
        print('N[%d] = %d' % (i, vet[i]))
    return


vetor = montarVetor()
trocaVetores(vetor)