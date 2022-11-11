#!/usr/bin/env python3.8
S = input()

for i in range(len(S) - 1, 0, -1):
  # print(S[:i])
  s = S[:i]
  if len(s) % 2 != 0:
    continue
  if s == s[:len(s)//2] * 2:
    print(len(s))
    exit()