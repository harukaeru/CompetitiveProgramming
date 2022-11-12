#!/usr/bin/env python3.8
s = input()
o = []

for c in s:
  if c == 'B':
    if len(o) != 0:
      o.pop()
  else:
    o.append(c)
  
print(''.join(o))