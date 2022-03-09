entrada1, entrada2, entrada3 = map(int, input().split())
if (entrada1 - entrada2) == 0 or (entrada1 - entrada3) == 0 or (entrada3 - entrada2) == 0:
    print('S')
elif (entrada1 + entrada2 - entrada3) == 0 or (entrada1 + entrada3 - entrada2) == 0 or (entrada2 + entrada3 - entrada1) == 0:
    print('S')
else:
    print('N')