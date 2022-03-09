def revisao(teclas, contratos):
    x = teclas
    y = contratos
    while x != '0' and y != '0':
        conta(x, y)
        x, y = input().split()


def conta(x2 ,y2):
    y2 = '0' + y2
    valor = int(y2.replace(x2, ''))
    return print(valor)


tecla, contrato = input().split()
revisao(tecla, contrato)
