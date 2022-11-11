#!/usr/bin/env python3.8
S = input()

alpha = [chr(ord('a') + i) for i in range(0, 26)]

S = set(S)
for a in alpha:
  if a not in S:
    print(a)
    exit()

print('None')

