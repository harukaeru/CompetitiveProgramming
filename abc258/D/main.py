#!/usr/bin/env python3.8
N, X = map(int, input().split())
AB = []
for i in range(N):
  a, b = map(int, input().split())
  AB.append((a, b))

S = []
s = 0
for i in range(N):
  s += AB[i][0] + AB[i][1]
  S.append(s)

m = 9999999999999999999999999999
for i in range(N):
  c = i + 1
  if X <= c:
    m = min(m, S[i])
  else:
    m = min(m, S[i] + (X - c) * AB[i][1])

# print(S)
print(m)