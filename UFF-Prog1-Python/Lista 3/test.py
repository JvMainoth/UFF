def printVet (imp, par):
    novoImp = imp
    novoPar = par
    contI = 0
    contP = 0
    for i in range(len(novoImp)):
        contI += 1
        if contI > 4:
            for i2 in range(len(novoImp)):
                print(f'par[{i2}] = {novoImp[i2]}')
            novoImp = []
            contI = 0
    for l in range(len(novoPar)):
        contP += 1
        if contP > 4:
            for l2 in range(len(novoPar)):
                print(f'par[{l2}] = {novoPar[l2]}')
            novoPar = []
            contP = 0
    return impar = []