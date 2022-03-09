a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

a2 = 0
b2 = 0
c2 = 0

if a >= b and a >= c:
    a2 = a
    if b >= c:
        b2 = b
        c2 = c
    else:
        c2 = b
        b2 = c

if b >= a and b >= c:
    a2 = b
    if a >= c:
        b2 = a
        c2 = c
    else:
        c2 = a
        b2 = c

if c >= a and c >= b:
    a2 = c
    if a >= b:
        b2 = a
        c2 = b
    else:
        c2 = a
        b2 = b

if a2 >= (b2 + c2):
    print("NAO FORMA TRIANGULO")

else:
    if (a2 ** 2) == ((b2 ** 2) + (c2 ** 2)):
        print("TRIANGULO RETANGULO")

    if (a2 ** 2) > ((b2 ** 2) + (c2 ** 2)):
        print("TRIANGULO OBTUSANGULO")

    if (a2 ** 2) < ((b2 ** 2) + (c2 ** 2)):
        print("TRIANGULO ACUTANGULO")

    if a2 == b2 == c2:
        print("TRIANGULO EQUILATERO")

    if a2 == b2 != c2 or b2 == c2 != a2 or c2 == a2 != b2:
        print("TRIANGULO ISOSCELES")






