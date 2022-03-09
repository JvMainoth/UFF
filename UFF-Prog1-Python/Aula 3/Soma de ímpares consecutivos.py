x = int(input())
y = int(input())
impar = 0

for z in range((y+1), x):
    if z % 2 != 0:
        impar += z
print(impar)
