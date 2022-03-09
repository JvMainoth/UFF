a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
ht = 0
mt = 0

if a < c:
    ht = c - a
    if b < d:
        mt = d - b
    elif b > d:
        ht = ht - 1
        mt = (60 - b) + d
    elif b == d:
        mt = 0
if a > c:
    ht = (24 - a) + c
    if b < d:
        mt = d - b
    elif b > d:
        ht = ht - 1
        mt = (60 - b) + d
    elif b == d:
        mt = 0
if a == c:
    if b < d:
        mt = d - b
        h = 0
    elif b > d:
        mt = (60 - b) + d
        ht = 23
    elif b == d:
        ht = 24
        mt = 0


print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (ht, mt))
