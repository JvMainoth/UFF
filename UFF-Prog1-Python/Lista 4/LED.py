def numTestes(test):
    while test > 0:
        test -= 1
        sequencia = input()
        leds(sequencia)
    return None

def leds(num):
    led = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    ledsTotal = 0
    for i in num:
        i2 = int(i)
        ledsTotal += led[i2]
    return print('%d leds' % ledsTotal)


testes = int(input())
numTestes(testes)