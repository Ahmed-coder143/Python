def func(x):
    if x>0:
      return "positive"
    elif x<0:
         return "negative"
    else:
        return "zero"
result=func(int(input("enter the number: ")))
print("The result is ",result)