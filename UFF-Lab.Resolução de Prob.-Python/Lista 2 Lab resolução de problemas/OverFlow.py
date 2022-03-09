max = int(input())
valor1, ope, valor2 = input().split()
valor1 = int(valor1)
valor2 = int(valor2)
if ope == "+":
    resul = valor1 + valor2
elif ope == "*":
    resul = valor1 * valor2

if resul > max:
    print("OVERFLOW")
else:
    print("OK")