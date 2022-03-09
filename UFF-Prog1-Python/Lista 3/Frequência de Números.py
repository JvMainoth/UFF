def leitura(test):
    valores = {}
    for i in range(test):
        v = int(input())
        if v in valores:
            valores[v] += 1
        else:
            valores[v] = 1
    chaves = valores.keys()
    chaves = sorted(chaves)

    for k in chaves:
        print('%d aparece %d vez(es)' % (k, valores[k]))


testes = int(input())
leitura(testes)