c = int(input())
l = int(input())
if c % 2 != 0:
    if l % 2 != 0:
        print("1")
    else:
        print("0")
elif c % 2 == 0:
    if l % 2 == 0:
        print("1")
    else:
        print("0")
