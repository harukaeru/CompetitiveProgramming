#!/usr/bin/env python3.8
S = input()
N = int(input())

a = (N - 1) // len(S)
b = (N - 1) % len(S)

print(S[a] + S[b])