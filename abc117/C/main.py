#!/usr/bin/env python3
N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

d = []
for i in range(M - 1):
  d.append(abs(X[i + 1] - X[i]))

d.sort()
d.reverse()
new_d = d[N - 1:]

print(sum(new_d))