y = int(input("Please write a number: "))

x = y

while x > 0:
    z = y % x
    if z == 0:
        print(x)
    x -= 1        ### x = x - 1


