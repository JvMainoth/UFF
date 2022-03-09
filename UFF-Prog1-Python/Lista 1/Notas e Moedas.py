valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for i in notas:
    troco = int(valor / i)
    print('{} nota(s) de R$ {:.2f}'.format(troco, i))
    valor -= troco * i

print('MOEDAS:')
for i in moedas:
    valor = round(valor, 2)
    troco = int(valor / i)
    print('{} moeda(s) de R$ {:.2f}'.format(troco, i))
    valor -= troco * i


