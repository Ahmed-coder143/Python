# Function to check if the parentheses are balanced
def is_balanced(parentheses_str):
    stack = []

    for char in parentheses_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack

# Input: String of parentheses
parentheses_input = input("Enter a string of parentheses: ")

# Check if the parentheses are balanced and print the result
if is_balanced(parentheses_input):
    print("yes")
else:
    print("no")
