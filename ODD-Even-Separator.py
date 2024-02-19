User_input=input("Enter the number: ")
i=[]
j=[]
a=[int(a) for a in str(User_input)]
#a=[for a in str(x)]
for value in a:
    if  value%2==0:
        i.append(value)
    else:
        j.append(value)
print("The result of even number is: ",*i)
print("The result of odd number is: ",*j)