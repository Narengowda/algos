def lps(seq, i, j):
    if i == j:
        return 1

    if len(seq) == 2 and seq[0] == seq[1]:
        return 2

    if seq[i] == seq[j]:
        return lps(seq, i + 1, j - 1) + 2

    return max(lps(seq, i + 1, j), lps(seq, i, j - 1))


inp = "goodogodf"
print(lps(inp, 0, len(inp) - 1))
