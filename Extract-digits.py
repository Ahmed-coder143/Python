number=int(input("Enter the number: "))
values=[int(a)for a in str(number)]
print("The digits are : ",*values)