number=input("enter the number: ")
even_digits=[]
odd_digits=[]
a=[int(a) for a in str(number)]
for value in a:
     if value%2==0:
         even_digits.append(value)
     else:
         odd_digits.append(value)
print("Sorted Even Digits: ",*sorted(even_digits))
print("Sorted Odd Digits: ",*sorted(odd_digits))