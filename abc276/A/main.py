#!/usr/bin/env python3.8
S = input()

n = -1
for i in range(len(S)):
  if S[i] == 'a':
    n = i + 1
print(n)