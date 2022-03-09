
valores = [0] * 3
for i in range(len(valores)):
    valores[i] = int(input())

valores_calculados = []
valores_calculados.append(valores[0] * 4 + valores[1] * 2)
valores_calculados.append(valores[0] * 2 + valores[2] * 2)
valores_calculados.append(valores[2] * 4 + valores[1] * 2)

print(min(valores_calculados))