number=int(input("Enter the size of the array: "))
arr=list(map(int,(input("Enter the array elements: ").split())))
value=set()
result=[]
for i in arr:
   if i not in value:
      value.add(i)
      result.append(i)
print("Array after removing duplicates: ",*result)