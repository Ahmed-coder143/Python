s = input("Enter a string: ")
n = len(s)

# Create a table to store the lengths of palindromes
table = [[0] * n for _ in range(n)]

# All substrings of length 1 are palindromes
for i in range(n):
    table[i][i] = 1

# Check all substrings of length 2
for i in range(n - 1):
    if s[i] == s[i + 1]:
        table[i][i + 1] = 2

# Check all substrings of length 3 and more
for cl in range(3, n + 1):
    for i in range(n - cl + 1):
        j = i + cl - 1
        if s[i] == s[j] and table[i + 1][j - 1] == cl - 2:
            table[i][j] = cl

# Find the maximum length in the table
max_length = max(max(row) for row in table)

# Output
print("The length of the longest palindromic substring is:",max_length)
