def montarMatriz():
    linhas = 12
    colunas = 12
    matris = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input()))
        matris.append(linha)
    return matris


def operacaoMatriz(ope, mat):
    soma = 0
    cont = 1
    cont2 = 0
    if ope == 'S':
        for i in range(0, 11):
            for i2 in range (cont, 12):
                soma += mat[i][i2]
            cont += 1
        print('%.1f' % soma)
    elif ope == 'M':
        for l in range(0, 11):
            for l2 in range(cont, 12):
                soma += mat[l][l2]
                cont2 += 1
            cont += 1
        media = soma/cont2
        print('%.1f' % media)
    return None



operacao = input()
matriz = montarMatriz()
operacaoMatriz(operacao, matriz)