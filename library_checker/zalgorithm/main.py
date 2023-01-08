#!/usr/bin/env python3.8
S = input()
Z = [len(S)]
i = 1
j = 0
while i < len(S):
    while i + j < len(S) and S[j] == S[i + j]:
        j += 1
    Z.append(j)
    print(i,j, ':', Z)

    if j == 0:
        i += 1
        continue

    k = 1
    while k < j and k + Z[k] < j:
        Z.append(Z[k])
        k += 1
    i += k
    j -= k
print(*Z)
