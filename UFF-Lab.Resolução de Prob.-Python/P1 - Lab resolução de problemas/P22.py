testes = int(input())
cont = 0
variante = 2
lista_resultados = [4]

for i in range(0, 20):
    variante += 2 ** i
    pedacos = variante ** 2
    lista_resultados.append(pedacos)

while 0 <= testes <= 20:
    cont += 1
    print(f'Teste {cont}')
    print(lista_resultados[testes])
    print()
    testes = int(input())

