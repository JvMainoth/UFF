cont = 1
participantes = int(input())
while participantes != 0:
    entradas = list(map(int,input().split()))
    for i in range(participantes):
        if entradas[i] == i+1:
            print("Teste", cont)
            cont += 1
            print(i+1)
            print()
            participantes = int(input())


