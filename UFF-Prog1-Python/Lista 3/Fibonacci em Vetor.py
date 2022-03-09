def resultados(test):
    for i in range(test):
        num = int(input())
        inicio = [0, 1]
        if num > 1:
            for i2 in range(2, num + 1):
                inicio.append(inicio[i2 - 2] + inicio[i2 - 1])
            print('Fib(%d) = %d' % (num, inicio[num]))
        elif num <= 1:
            print('Fib(%d) = %d' % (num, inicio[num]))
    return None


testes = int(input())
resultados(testes)