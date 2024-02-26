number = int(input("Enter the number: "))
ordered_number = int(''.join(sorted(str(number), reverse=True)))

print("The ordered number is: ",ordered_number)