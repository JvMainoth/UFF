def fazerPeriodos(per):
    while per != 'Fim dos Períodos':
        inicio, fim = list(map(int, per.split()))
        maior = 0
        aplicacao = ''
        for i in range(len(aplicacaoResultados)):
            for x in vetorResultados(i, inicio, fim):
                if x > maior:
                    maior = x
                    aplicacao = aplicacaoResultados[i][0]
        print(f'Entre os meses {inicio} e {fim}, a melhor aplicação foi:{aplicacao}')
        print(f'Com maior percentual mensal médio no período de: {maior:1.3f}')
        per = input()


def vetorResultados(indice, start, end):
    soma = 0
    listaSoma = []
    for i in aplicacaoResultados[indice][start:end + 1]:
        val = float(i)
        soma += val
    listaSoma.append(soma / len(aplicacaoResultados[indice][start:end + 1]))
    return listaSoma


aplicacaoResultados = [] # n era pra ter definido isto aqui.
linhas = input().replace('#', ' ')
while linhas != 'Fim das Opções':
    aplicacaoResultados.append(linhas.split())
    linhas = input().replace('#', ' ')
periodos = input()
fazerPeriodos(periodos)