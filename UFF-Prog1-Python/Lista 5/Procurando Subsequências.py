def procura ():
    caso = 1
    while True:
        try:
            num1 = input()
            num2 = input()
            print('Caso #%d:' % caso)
            quanti = num2.count(num1)
            if quanti == 0:
                print('Nao existe subsequencia')
            else:
                print('Qtd.Subsequencias: %d' % quanti)
                quanti = num2.rfind(num1)
                print('Pos: %d' % (int(quanti) + 1))
            print()
            caso += 1

        except EOFError:
            break


procura()