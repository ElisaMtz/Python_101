y = int(input("Please write first number: "))
w = int(input("Please write second number: "))

if y >= w:
    x = w
else:
    x = y

while x > 0:
    z1 = y % x
    z2 = w % x

    if z1 == 0 and z2 == 0:
        print(x)
        break
    x -= 1        ### x = x - 1


