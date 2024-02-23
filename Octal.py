Binary_number = input("Enter a binary number: ")
Decimal_number = int(Binary_number, 2)
Octal_number = oct(Decimal_number)[2:]
print(f"The Octal equivalent of {Binary_number} is: {Octal_number}")