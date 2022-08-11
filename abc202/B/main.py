#!/usr/bin/env python3
S = input()

S = S[::-1]

table = {
  '0': '0',
  '1': '1',
  '6': '9',
  '8': '8',
  '9': '6',
}
c = []
for s in S:
  c.append(table[s])

print(''.join(c))