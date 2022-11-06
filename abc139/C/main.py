#!/usr/bin/env python3.8
N = int(input())
H = list(map(int, input().split()))

increaser = [0]
for i in range(N - 1):
  if H[i + 1] <= H[i]:
    increaser.append(increaser[i] + 1)
  else:
    increaser.append(0)

print(max(increaser))