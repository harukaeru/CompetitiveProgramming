#!/usr/bin/env python3
N, X = map(int, input().split())
S = input()

b = list(bin(X)[2:])
# print(b)

for s in S:
  if s == 'U':
    if b:
      b.pop()
  elif s == 'L':
    b.append('0')
  else:
    b.append('1')

print(int('0b' + ''.join(b), 2))