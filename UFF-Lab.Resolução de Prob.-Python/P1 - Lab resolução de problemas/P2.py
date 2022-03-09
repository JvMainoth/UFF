testes = int(input())
cont = 0
pedacos = 2
while 0 <= testes <= 20:
    pedacos += 2 ** testes
    pedacoss = pedacos ** 2
    cont += 1
    print(f'Teste {cont}')
    print(pedacoss)
    print()
    testes = int(input())


