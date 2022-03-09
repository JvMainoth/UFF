def montarVetor():
    valores = [None] * 10
    for i in range(10):
        valores[i] = int(input())
    return valores

def substituicao(vet):
    for i in range(len(vet)):
        num = vet[i]
        if num <= 0:
            vet[i] = 1
        print('X[%d] = %d' % (i, vet[i]))
    return None



vetor = montarVetor()
(vetosubstituicaor)