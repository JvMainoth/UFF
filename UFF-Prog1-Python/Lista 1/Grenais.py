novoGrenal = 1
cont = 0
vitoriasInt = 0
vitoriasGre = 0
empates = 0

while novoGrenal == 1:
    cont += 1
    golsInter, golsGremio = input().split()
    golsInter, golsGremio = int(golsInter), int(golsGremio)

    if golsInter > golsGremio:
        vitoriasInt += 1
    elif golsGremio > golsInter:
        vitoriasGre += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    novoGrenal = int(input())

print("%d grenais" % cont)
print("Inter:%d" % vitoriasInt)
print("Gremio:%d" % vitoriasGre)
print("Empates:%d" % empates)

if vitoriasInt>vitoriasGre:
    print('Inter venceu mais')
elif vitoriasGre>vitoriasInt:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')





