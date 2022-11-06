#!/usr/bin/env python3.8
N = int(input())
S = list(map(int, input().split()))

def check(s):
  is_ng = True
  for a in range(1, 501):
    for b in range(1, 501):
      if s == 4 * a * b + 3 * a + 3 * b:
        is_ng = False
        return is_ng
  return is_ng


cnt = 0
for s in S:
  cnt += check(s)

print(cnt)
