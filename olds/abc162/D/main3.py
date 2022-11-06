#!/usr/bin/env python3.8
N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')

s = r * g * b

cons = {'R', 'G', 'B'}

for i in range(N):
    for j in range(i + 1, N):
        k = (j + j - i)
        if k < N and ({S[i], S[j], S[k]} == cons):
            # print('(i,j,k)', i, j, k)
            s -= 1

print(s)
