#Hexadecimal
Binary_number = input("Enter a binary number: ")
Decimal_number = int(Binary_number, 2)
Hexadecimal_number = hex(Decimal_number)[2:]
print(f"The hexadecimal equivalent of {Binary_number} is: {Hexadecimal_number}")
