def montarVetor():
    valores = []
    for i in range(100):
        valores.append(float(input()))
    return valores


def resultado(vet):
    for i in range(len(vet)):
        if vet[i] <= 10:
            print('A[%d] = %.1f' % (i, vet[i]))



vetor = montarVetor()
resultado(vetor)