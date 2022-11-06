#!/usr/bin/env python3.8

S = input()
T = input()

for n in range(1, 27):
  candidate = ''
  for s in S:
    alpha_num = ord(s) - ord('a')
    real_n = (alpha_num + n) % 26
    c = chr(ord('a') + real_n)
    candidate += c
  if T == candidate:
    print('Yes')
    exit()
print('No')