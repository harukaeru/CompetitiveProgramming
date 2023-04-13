#!/usr/bin/env python3.8
S = input()

x = None
y = None
for i in range(len(S)):
  if S[i] == 'B':
    if x is None:
      x = i
    else:
      y = i

inner = False
cond2 = False

for i in range(len(S)):
  if S[i] == 'R':
    if not inner:
      inner = True
    else:
      inner = False
  else:
    if S[i] == 'K' and inner:
      cond2 = True

cond1 = x % 2 != y % 2

if cond1 and cond2:
  print('Yes')
else:
  print('No')
