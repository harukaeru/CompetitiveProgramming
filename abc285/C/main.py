#!/usr/bin/env python3.8
S = input()

d = len(S)

S = S[::-1]

tot = 0
for i in range(d):
  num = ord(S[i]) - ord('A') + 1
  tot += num * (26 ** i)

print(tot)