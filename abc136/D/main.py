#!/usr/bin/env python3.8
from bisect import bisect_left


S = input()

L = []
R = []
for i in range(len(S)):
  if S[i] == 'L':
    L.append(i)
  else:
    R.append(-i)

R.sort()

anses = [0] * len(S)
for i in range(len(S)):
  if S[i] == 'R':
    t = bisect_left(L, i)
    # print('t', i, '->', L[t])
    target = L[t]
    dist = target - i
    if dist % 2 == 0:
      anses[target] += 1
    else:
      anses[target - 1] += 1
  else:
    t = bisect_left(R, -i)
    # print('t', i, '->', -R[t])
    target = -R[t]
    dist = i - target
    if dist % 2 == 0:
      anses[target] += 1
    else:
      anses[target + 1] += 1
# print(L)
# print(R)
print(*anses)