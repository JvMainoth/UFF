vetor = []
linhas = input().replace('#', ' ')
while linhas != 'Fim das Opções':
    vetor.append(linhas.split())
    linhas = input().replace('#', ' ')
periodo = input()
while periodo != 'Fim dos Períodos':
    inicio, fim = list(map(int, periodo.split()))
    soma = 0
    resultadofinal = []
    maior = 0
    aplicacao = ''
    for d in range(len(vetor)):
        for i in vetor[d][inicio:fim + 1]:
            numero = float(i)
            soma += numero
        resultadofinal.append(soma / len(vetor[d][inicio:fim + 1]))
        soma = 0
        for x in resultadofinal:
            if x > maior:
                maior = x
                aplicacao = vetor[d][0]
    print(f'Entre os meses {inicio} e {fim}, a melhor aplicação foi:{aplicacao}')
    print(f'Com maior percentual mesal médio no período de: {maior:1.3f}')
    periodo = input()



