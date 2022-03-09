pedacos = [4]
raiz = 2
for i in range(0, 20):
    raiz += 2**i
    num_pedacos = raiz**2
    pedacos.append(num_pedacos)

contador = 0
teste = int(input())
while teste != -1:
    contador += 1
    print('Teste %d' % contador)
    print(pedacos[teste])
    print('')
    teste = int(input())