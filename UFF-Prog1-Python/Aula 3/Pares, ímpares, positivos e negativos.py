a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
pares = 0
impar = 0
positivo = 0
negativo = 0

for valor1 in (a, b, c, d, e):
    if valor1 % 2 == 0:
        pares += 1
        if valor1 > 0:
            positivo += 1
        elif valor1 < 0:
            negativo += 1
    elif valor1 % 2 != 0:
        impar += 1
        if valor1 > 0:
            positivo += 1
        elif valor1 < 0:
            negativo += 1
print("%d valor(es) par(es)" % pares)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % positivo)
print("%d valor(es) negativo(s)" % negativo)
