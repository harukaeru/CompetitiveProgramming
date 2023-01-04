#!/usr/bin/env python3.8
from collections import Counter
import math

N = int(input())

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

fact = factorization(N)
counter = Counter()
for v in fact:
  counter[v[0]] = v[1]

keys = list(counter.keys())
keys.sort()

cnt = 0
for i in keys:
  c = 1
  while counter[i] >= c and N > 1:
    N //= c
    counter[i] -= c
    c += 1
    cnt += 1

  if N == 1:
    break

print(cnt)