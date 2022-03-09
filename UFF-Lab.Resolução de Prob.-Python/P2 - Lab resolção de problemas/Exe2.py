n = int(input())
linha = input()
num = linha.split()
c1 = []
c2 = [0]
for i in range(n):
    c1.append(int(num[i]))

c1.sort()
for i in c1:
    if i - c2[-1] <= 8:
        c2.append(i)
    else:
        print("N")
        break
c2.remove(0)
if c1 == c2:
    print("S")





