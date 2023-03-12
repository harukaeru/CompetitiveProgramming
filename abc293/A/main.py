#!/usr/bin/env python3.8
S = list(input())
for i in range(1, len(S) // 2 + 1):
  a = i * 2 - 1 - 1
  b = i * 2 - 1
  S[a],S[b] = S[b], S[a]
  # print(S)

print(''.join(S))