def fib(int, n):
    global cont
    cont += 1
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


c = int(input())
b = int(input())
inter = fib(c, b)
cont = 0
print("fib(%d) = %d " % b, cont-1)
print("calls = %d\n" % inter)
