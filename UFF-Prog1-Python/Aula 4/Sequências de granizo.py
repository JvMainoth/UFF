valor = int(input())
while valor != 0:
    if 1 <= valor <= 500:
        valores = [valor]
        while valor != 1:
            if valor % 2 == 0:
                valor = int(1 / 2 * valor)
                valores.append(valor)

            elif valor % 2 != 0:
                valor = 3 * valor + 1
                valores.append(valor)
        print(max(valores))
    valor = int(input())




