y = input("Please enter a number: ")

y = int(y)

total, x = 0, 1

while x <= y:
    total += x
    x += 1        ### x = x +1
print(total)