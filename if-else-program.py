number1=int(input("enter the number1: "))
number2=int(input("enter the number2: "))
number3=int(input("enter the number3: "))
if number1>number2 and number1>number3:
   print("The maximum number:",number1)
elif number2>number3:
   print("The maximum number:",number2)
else:
    print("The maximum number:",number3)