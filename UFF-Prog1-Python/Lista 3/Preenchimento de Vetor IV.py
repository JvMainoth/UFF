def montarVetor():
    impar = []
    par = []
    cont = 0
    contI = 0
    contP = 0
    while cont < 15:
        num = int(input())
        cont += 1
        if num % 2 == 1:
            impar.append(num)
            contI += 1
        elif num % 2 == 0:
            par.append(num)
            contP += 1
        if contI > 4:
            for i2 in range(len(impar)):
                print('impar[%d] = %d' % (i2, impar[i2]))
            impar = []
            contI = 0
        if contP > 4:
            for l2 in range(len(par)):
                print('par[%d] = %d' % (l2, par[l2]))
            par = []
            contP = 0
    contFinal(impar, par)
    return

def contFinal (imp, pa):
    for i in range(len(imp)):
        print('impar[%d] = %d' % (i, imp[i]))
    for i2 in range(len(pa)):
        print('par[%d] = %d' % (i2, pa[i2]))
    return


montarVetor()