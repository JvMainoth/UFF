def contaMedalha(med):
    o = p = b = 0
    if med == 'ouro':
        o += 1
    elif med == 'prata':
        p += 1
    elif med == 'bronze':
        b += 1
    return o, p, b


qtdMedalhasDisputadas = int(input())
paises = []
desempenhos = []
for n in range(qtdMedalhasDisputadas):
    qtdOuro = qtdPrata = qtdBronze = 0
    resultados = input().split('#')
    pais = resultados[0]
    medalha = resultados[1]
    modalidade = resultados[2]
    qtdOuro, qtdPrata, qtdBronze = contaMedalha(medalha)
    if pais not in paises:
        paises.append(pais)
        desempenho = [pais, qtdOuro, qtdPrata, qtdBronze]
        desempenhos.append(desempenho)
    else:
        print(qtdPrata)
        for d in desempenhos:
            for i in d:
                if d[0] == pais:
                    d[1] += qtdOuro
                    d[2] += qtdPrata
                    d[3] += qtdBronze

print(desempenhos)