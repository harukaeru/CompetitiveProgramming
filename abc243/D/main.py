#!/usr/bin/env python3.8
N, X = map(int, input().split())
S = input()

T = []
for s in S:
  if len(T) == 0:
    T.append(s)
    continue

  t = T.pop()
  if (t == 'L' or t == 'R') and s == 'U':
    continue
  T.append(t)
  T.append(s)

# print(T)

for t in T:
  if t == 'U':
    X = max(1, X // 2)
  elif t == 'L':
    X = X * 2
  elif t == 'R':
    X = X * 2 + 1

print(X)