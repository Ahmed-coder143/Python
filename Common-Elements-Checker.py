list1=list(map(int,(input("Enter the list of numbers: ").split())))
list2=list(map(int,(input("Enter the list of numbers: ").split())))
print(*list1)
print(*list2)
value=set(list1)&set(list2)
print(*value)
if value:
    print("Common elements: yes")
else:
    print("Common elements: no")