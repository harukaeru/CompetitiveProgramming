#!/usr/bin/env python3.8
O = input()
E = input()

p = ''
for i in range(len(O) + len(E)):
  if i % 2 == 0:
    p += O[i // 2]
  else:
    p += E[i // 2]

print(p)