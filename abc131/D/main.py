#!/usr/bin/env python3.8
N = int(input())
T = []
for i in range(N):
  a, b = map(int, input().split())
  T.append((b, -a))

T.sort()
# print(T)

c = 0
for t in T:
  p = -t[1]
  c += p
  if t[0] < c:
    print('No')
    exit()
print('Yes')
