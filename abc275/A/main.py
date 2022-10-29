#!/usr/bin/env python3
N = int(input())
H = list(map(int, input().split()))

m = -1
mi = -1
for i in range(N):
  if m < H[i]:
    m = H[i]
    mi = i

print(mi + 1)