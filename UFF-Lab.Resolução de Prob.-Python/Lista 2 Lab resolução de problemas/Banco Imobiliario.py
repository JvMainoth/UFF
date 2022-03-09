dinheiro, operacoes = map(int, input().split())
dalia = dinheiro
eloi = dinheiro
felix = dinheiro
while operacoes != 0:
    transacoes = list(input().split())
    if transacoes[0] == "C":
        if transacoes[1] == "D":
            valor = int(transacoes[2])
            dalia -= valor
        elif transacoes[1] == "E":
            valor = int(transacoes[2])
            eloi -= valor
        elif transacoes[1] == "F":
            valor = int(transacoes[2])
            felix -= valor
    elif transacoes[0] == "V":
        if transacoes[1] == "D":
            valor = int(transacoes[2])
            dalia += valor
        elif transacoes[1] == "E":
            valor = int(transacoes[2])
            eloi += valor
        elif transacoes[1] == "F":
            valor = int(transacoes[2])
            felix += valor
    elif transacoes[0] == "A":
        if transacoes[1] == "D" and transacoes[2] == "E":
            valor = int(transacoes[3])
            dalia += valor
            eloi -= valor
        if transacoes[1] == "D" and transacoes[2] == "F":
            valor = int(transacoes[3])
            dalia += valor
            felix -= valor
        if transacoes[1] == "E" and transacoes[2] == "D":
            valor = int(transacoes[3])
            dalia -= valor
            eloi += valor
        if transacoes[1] == "E" and transacoes[2] == "F":
            valor = int(transacoes[3])
            felix -= valor
            eloi += valor
        if transacoes[1] == "F" and transacoes[2] == "D":
            valor = int(transacoes[3])
            dalia -= valor
            felix += valor
        if transacoes[1] == "F" and transacoes[2] == "E":
            valor = int(transacoes[3])
            felix += valor
            eloi -= valor
    operacoes -= 1
print(dalia, eloi, felix)