def montarTabela (x):
    tabelaPais = []
    for i in range(x):
        info = input().split('#')
        #Ver qual é o pais e jogar na tabela
        if info[0] not in tabelaPais:
            tabelaPais.append(info[0])
            distribuirMedalha(tabelaPais, info, i)
    return None


def distribuirMedalha(ala, y, z):
    nova_Tbaela = [ala.split(), 0, 0, 0]
    if y[0] == ala[z][0]:
        if y[1] == 'ouro':
            ala[z][1] += 1
        if y[1] == 'prata':
            ala[z][2] += 1
        if y[1] == 'bronze':
            ala[z][3] += 1
    return None


#Input da quantidade de medalhas disputadas
disputas = int(input())
montarTabela(disputas)


#saida de acordo na ordem dos paises que entraram