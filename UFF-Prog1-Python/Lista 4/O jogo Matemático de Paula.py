def numTestes(test):
    while test > 0:
        test -= 1
        sequencia = input()
        game(sequencia)
    return None


def game(num):
    num1 = int(num[0])
    num2 = int(num[2])
    resultado = 0
    if num1 == num2:
        resultado = num1 * num2
    elif num[1].isupper():
        resultado = num2 - num1
    elif num[1].islower():
        resultado = num1 + num2
    return print(resultado)


testes = int(input())
numTestes(testes)