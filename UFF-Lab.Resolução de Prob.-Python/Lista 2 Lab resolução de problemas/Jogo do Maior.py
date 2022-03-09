teste = int(input())
while teste != 0:
    pontos_jg1 = 0
    pontos_jg2 = 0
    for i in range(teste):
        jogador1, jogador2 = map(int, input().split())
        if jogador1 > jogador2:
            pontos_jg1 += 1
        elif jogador2 > jogador1:
            pontos_jg2 += 1
    print(pontos_jg1, pontos_jg2)
    teste = int(input())
