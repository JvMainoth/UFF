x = int(input())
y = int(input())
total = 0
soma = 0
for i in range(x, y+1):
    if i % 13 != 0:
        soma = soma + i
        total = soma
    else:
        continue
print(total)
