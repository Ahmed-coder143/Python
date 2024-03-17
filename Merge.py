#Merge two list of numbers and sorted
arr1=list(map(int,(input("Enter the array1 numbers: ").split())))
arr2=list(map(int,(input("ENter the array2 numbers: ").split())))
value=arr1+arr2
print("Merged and Sorted Array: " ,*sorted(value))
