def preencher(x):
    cont = 0
    while cont < 2:
        x.append(float(input()))
        if x[len(x) - 1] > 0 and x[len(x) - 1] <= 10:
            cont += 1
        else:
            print('nota invalida')
    return None

def media(y):
    media = 0
    for i in y:
        if i > 0 and i <= 10:
            media += i
    media = media/2
    return print('media = %.2f' % media)


lista = []
preencher(lista)
media(lista)


