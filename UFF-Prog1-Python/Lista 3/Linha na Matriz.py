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


def operacaoMatriz(numLi, ope, mat):
    linha = []
    soma = 0
    media = 0
    for i in range(len(mat)):
        linha.append(mat[numLi][i])
    if ope == 'S':
        for i2 in linha:
            soma += i2
        print('%.1f' % soma)
    elif ope == 'M':
        for i3 in linha:
            soma += i3
            media = soma/len(linha)
        print('%.1f' % media)
    return None


linha = int(input())
operacao = input()
matriz = montarMatriz()
operacaoMatriz(linha, operacao, matriz)