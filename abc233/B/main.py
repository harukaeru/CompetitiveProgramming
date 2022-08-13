#!/usr/bin/env python3
L, R = map(int, input().split())
S = input()

L = L - 1
R = R - 1

t = S[L:R + 1][::-1]
print(S[0:L] + t + S[R + 1:])