#!/usr/bin/env python3.8
S = input()
T = int(input())

y = abs(S.count('U') - S.count('D'))
x = abs(S.count('R') - S.count('L'))
d = x + y
if T == 1:
  print(d + S.count('?'))
else:
  q = S.count('?')
  if y <= q:
    q -= y
    y = 0
  else:
    y -= q
    q = 0

  if x <= q:
    q -= x
    x = 0
  else:
    x -= q
    q = 0

  print(x + y + q % 2)