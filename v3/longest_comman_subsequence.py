A = "ABCDGH"
B = "AEDFHR"


def LCS(i, j):

    if i >= len(A) or j >= len(B):
        return 0

    if A[i] == B[j]:
        return 1 + LCS(i + 1, j + 1)

    return max(LCS(i + 1, j), LCS(i, j + 1))


print(LCS(0, 0))
