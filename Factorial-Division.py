import math

a,b =map(int,(input("Enter two integers separated by space: ").split()))

c = math.factorial(a) / math.factorial(b)
print("Result",int(c))