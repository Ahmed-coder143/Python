number=int(input("Enter the number: "))
Binary=bin(number)
result=Binary.count('1')
print((f"The number of '1's in the binary representation of {number} is: {result}"))