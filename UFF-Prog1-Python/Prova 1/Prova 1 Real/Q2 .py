def montarTabela (x):
    tabelaPais = []
    tabelaFinal = []
    for i in range(x):
        info = input().split('#')
        pais = info[0]
        medalha = info[1]
        medO, medP, medB = colocarmedalha(medalha)
        if pais not in tabelaPais:
            tabelaPais.append(pais)
            tabelaMedalha = [pais, medO, medP, medB]
            tabelaFinal.append(tabelaMedalha)
        else:
            for i2 in tabelaFinal:
                for i3 in i2:
                    if pais == i3:
                        i2[1] += medO
                        i2[2] += medP
                        i2[3] += medB
    return tabelaFinal

def colocarmedalha(x):
    b = 0
    p = 0
    o = 0
    if x == 'ouro':
         o += 1
    if x == 'prata':
        p += 1
    if x == 'bronze':
        b += 1
    return o, p, b


def formatartabela(x):
    print('Quadro de Medalhas das Olimpíadas de Tóquio:')
    for i in x:
        print(f'{tuple(i)}')


disputas = int(input())
tabela = montarTabela(disputas)
formatartabela(tabela)
