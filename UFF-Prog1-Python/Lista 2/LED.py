def numTeste (teste):
    while teste > 0:
        leds(teste)
        teste -= 1
    return None


def leds(lin):
    for j in range(1, lin+1):
        led = 0
        num = input()
        for i in range(0, len(num)):
            if num[i] == '1':
                led = led + 2
            if num[i] == '2':
                led = led + 5
            if num[i] == '3':
                led = led + 5
            if num[i] == '4':
                led = led + 4
            if num[i] == '5':
                led = led + 5
            if num[i] == '6':
                led = led + 6
            if num[i] == '7':
                led = led + 3
            if num[i] == '8':
                led = led + 7
            if num[i] == '9':
                led = led + 6
            if num[i] == '0':
                led = led + 6
        return print('%d leds' % led)


teste = int(input())
numTeste(teste)