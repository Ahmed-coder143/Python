def sum_ascii(x):
    total=sum(ord(char) for char in x)
    print(total)

y=input("Enter the user input: ")
result=sum_ascii(y)
