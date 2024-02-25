import math

def factorial(n):
    return math.factorial(n)

def find_gcd(A, B):
    if A <= B:
        return factorial(A)
    else:
        return factorial(B)


A, B = map(int, input().split())
result = find_gcd(A, B)
print(result)
