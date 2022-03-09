testes = int(input())

for i in range(testes):
    valor, encaixe = list(map(str,input().split()))
    if valor[-len(encaixe):] == encaixe:
        print("encaixa")
    else:
        print("nao encaixa")