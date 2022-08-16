#!/usr/bin/env python3
N = int(input())
a = list(map(int, input().split()))

cnt = 0
for x in a:
  while x > 0:
    if x % 2 == 0:
      cnt += 1
      x //= 2
    else:
      break

print(cnt)