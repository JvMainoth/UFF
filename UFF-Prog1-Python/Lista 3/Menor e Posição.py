def vetor(tam):
    valores = list(map(int, input().split()))
    for i in range(len(valores)):
        valores[i] = int(valores[i])

    menor = valores[0]
    posicao = 0
    for i2 in range(1, len(valores)):
        if valores[i2] < menor:
            menor = valores[i2]
            posicao = i2
    print('Menor valor: %d' % menor)
    print('Posicao: %d' % posicao)


tamanho = int(input())
vetor(tamanho)
