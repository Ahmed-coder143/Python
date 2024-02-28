def lcs_of_three_strings(X, Y, Z):
    m, n, o = len(X), len(Y), len(Z)

    # Create a 3D table to store the lengths of LCS
    L = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the table in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif X[i - 1] == Y[j - 1] == Z[k - 1]:
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(L[i - 1][j][k], L[i][j - 1][k], L[i][j][k - 1])

    # Reconstruct the LCS
    lcs = []
    i, j, k = m, n, o
    while i > 0 and j > 0 and k > 0:
        if X[i - 1] == Y[j - 1] == Z[k - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
            k -= 1
        elif L[i - 1][j][k] >= L[i][j - 1][k] and L[i - 1][j][k] >= L[i][j][k - 1]:
            i -= 1
        elif L[i][j - 1][k] >= L[i][j][k - 1]:
            j -= 1
        else:
            k -= 1

    return ''.join(reversed(lcs)) if lcs else -1

# Input
X, Y, Z = input("Enter separated strings: ").split()

# Output
result = lcs_of_three_strings(X, Y, Z)
print("The Longest Common Subsequence (LCS) for the three strings is: ",result)
