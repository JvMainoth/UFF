def montarVetor():
    valores = [0] * 10
    valores[0] = int(input())
    return valores


def multiplicacao(vet):
    for i in range(len(vet)):
        if vet[i] != vet[0]:
            vet[i] = vet[i - 1] * 2
        print('N[%d] = %d' % (i, vet[i]))
    return None


vetor = montarVetor()
multiplicacao(vetor)