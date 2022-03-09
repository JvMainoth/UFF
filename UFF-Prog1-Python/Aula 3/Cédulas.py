n = int(input())

nota100 = n // 100
nota50 = n % 100 // 50
nota20 = n % 100 % 50 // 20
nota10 = n % 100 % 50 % 20 // 10
nota5 = n % 100 % 50 % 20 % 10 // 5
nota2 = n % 100 % 50 % 20 % 10 % 5 // 2
nota1 = n % 100 % 50 % 20 % 10 % 5 % 2 // 1

print(n)
print("%d nota(s) de R$ 100,00" % nota100)
print("%d nota(s) de R$ 50,00" % nota50)
print("%d nota(s) de R$ 20,00" % nota20)
print("%d nota(s) de R$ 10,00" % nota10)
print("%d nota(s) de R$ 5,00" % nota5)
print("%d nota(s) de R$ 2,00" % nota2)
print("%d nota(s) de R$ 1,00" % nota1)
