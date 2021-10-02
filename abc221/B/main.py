#!/usr/bin/env python3
S = input()
T = input()

if S == T:
    print('Yes')
    exit()

S = list(S)
for i in range(len(S) - 1):
    newS = S[:i] + [S[i + 1], S[i]] + S[i+2:]
    s = ''.join(newS)
    if s == T:
        print('Yes')
        exit()
print('No')
