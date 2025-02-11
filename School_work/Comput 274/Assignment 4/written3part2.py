def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]  # Copy i-th element of S1 as next item of S
            i += 1
        else:
            S[i + j] = S2[j]  # Copy j-th element of S2 as next item of S
            j += 1