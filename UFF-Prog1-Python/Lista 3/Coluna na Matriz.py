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


def operacaoMatriz(numCo, ope, mat):
    coluna = []
    soma = 0
    media = 0
    for i in range(len(mat)):
        coluna.append(mat[i][numCo])
    if ope == 'S':
        for i2 in coluna:
            soma += i2
        print('%.1f' % soma)
    elif ope == 'M':
        for i3 in coluna:
            soma += i3
            media = soma/len(coluna)
        print('%.1f' % media)
    return None


testes = int(input())
operacao = input()
matriz = montarMatriz()
operacaoMatriz(testes, operacao, matriz)