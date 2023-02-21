#!/usr/bin/env python3.8
N = int(input())
C = list(map(int, input().split()))

length = N // min(C)
ans = ''

for i in range(length):
  rest = length - i - 1

  for j in range(8, -1, -1):
    if min(C) * rest + C[j] <= N:
      ans += str(j + 1)
      N -= C[j]
      break

print(ans)