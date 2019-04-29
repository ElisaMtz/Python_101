x = int(input("Please write first number: "))
y = int(input("Please write second number: "))

temp = x * y

if x >= y:
    big = y
else:
    big = x

while True:
    if(big % x == 0) and (big % y == 0):
        temp = big
        break
    big += 1

print(temp)