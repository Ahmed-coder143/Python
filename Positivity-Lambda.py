func=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
result=func(int(input("enter the number: ")))
print("The result is ",result)