#!/usr/bin/env python3.8
# 素因数分解
from collections import Counter
mod = 10 **9 + 7


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

N = int(input())
counter = Counter()
for i in range(1, N + 1):
  for fact in factorization(i):
    counter[fact[0]] += fact[1]

cnt = 1
# print(counter)
for k, v in counter.items():
  if k == 1:
    continue
  cnt *= (v + 1)
  cnt %= mod
print(cnt)