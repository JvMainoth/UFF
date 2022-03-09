def numTestes(test):
    while test > 0:
        test -= 1
        sequencia = int(input())
        fibonacci(sequencia)
    return None


def fibonacci(num):
    lista = [1, 1]
    fib = [0, 1]
    for i in range(2, 41):
        lista.append(lista[i - 1] + lista[i - 2] + 1)
        fib.append(fib[i - 1] + fib[i - 2])
    return print("fib(%d) = %d calls = %d" % (num, lista[num] - 1, fib[num]))


testes = int(input())
numTestes(testes)