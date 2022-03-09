ten = int(input())
rodadas = 0
partidas1 = 0
partidas2 = 0

while ten > 1:
    rodadas += 1
    partidas1 = ten//2
    partidas2 = partidas1 + partidas2
    ten = ten/2

print(partidas2)
print(rodadas)


