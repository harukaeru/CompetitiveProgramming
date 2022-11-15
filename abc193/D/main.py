#!/usr/bin/env python3.8
from collections import defaultdict
K = int(input())
S = input()
T = input()

CS = defaultdict(int)
CT = defaultdict(int)
ss = 0
tt = 0
for i in range(len(S) - 1):
  s = int(S[i])
  t = int(T[i])
  CS[s] += 1
  CT[t] += 1

for i in range(1, 10):
  v = CS[i]
  ss += i * (10 ** v)

for i in range(1, 10):
  v = CT[i]
  tt += i * (10 ** v)

PC = []
for i in range(1, 10):
  rest = K - CS[i] - CT[i]
  if rest > 0:
    prev = i * (10 ** CS[i])
    cur = i * (10 ** (CS[i] + 1))
    PC.append((ss - prev + cur, rest, i))

PT = []
for i in range(1, 10):
  rest = K - CS[i] - CT[i]
  if rest > 0:
    prev = i * (10 ** CT[i])
    cur = i * (10 ** (CT[i] + 1))
    PT.append((tt - prev + cur, rest, i))

tot = 0
win = 0
lose = 0
for i, pc in enumerate(PC):
  for j, pt in enumerate(PT):
    dpt = pt[1]
    if i == j:
      dpt -= 1
    if pc[0] > pt[0]:
      win += pc[1] * dpt
    else:
      lose += pc[1] * dpt
    tot += pc[1] * dpt

print(win / tot)