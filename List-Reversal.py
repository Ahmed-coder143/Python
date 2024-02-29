# Function to reverse and print the list
def reverse_and_print(lst):
    reversed_list = lst[::-1]
    print("->".join(map(str, reversed_list)))

# Input: Number of elements
N = int(input("Enter the number of elements: "))

# Input: List of N numbers
numbers = list(map(int, input("Enter the list of numbers separated by space: ").split()))

# Check if the input size constraint is satisfied
if 1 <= N <= 10000:
    # Reverse and print the list
    reverse_and_print(numbers)
else:
    print("Input size out of bounds. Please ensure 1 <= N <= 10000.")
