#Sum of digits
number=int(input("Enter the number: "))
sum=0
while number>0:
  sum=sum+number%10
  number=number//10
print("The sum of value is",sum)
