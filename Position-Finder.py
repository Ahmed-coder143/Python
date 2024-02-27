
num = int(input("Enter an integer: "))


position = 0
while num > 0:
    position += 1
    if num % 2 == 1:
        break
    num //= 2


print("Position of the rightmost '1' in binary:", position)
