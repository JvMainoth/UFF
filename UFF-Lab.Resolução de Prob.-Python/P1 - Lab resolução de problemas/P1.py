jogadores, turnos = map(int, input().split())
valores = list(map(int, input().split()))
# Armazenando os pontos
pontos = [0] * jogadores
vencedor = 0
maior = 0

for i in range(jogadores):
    pontos[i] = sum(valores[i::jogadores])

for i2 in range(len(pontos)):
    if pontos[i2] >= maior:
        maior = pontos[i2]
        vencedor = i2 + 1
print(vencedor)