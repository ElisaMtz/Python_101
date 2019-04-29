y = int(input("Please write a number: "))

total = 1

while y > 0:
    total *= y
    y -= 1        ### x = x - 1
print(total)