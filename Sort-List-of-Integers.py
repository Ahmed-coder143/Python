user_input=int(input("enter the number: "))
arr=list(map(int,(input("enter the list of integers: ").split())))
print(*sorted(arr))