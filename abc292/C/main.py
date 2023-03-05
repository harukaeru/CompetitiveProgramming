#!/usr/bin/env python3.8
N = int(input())

cache = {}

def factorization(n):
    if n == 1:
      return 1
    if cache.get(n):
      return cache[n]

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

    res = 1
    for a in arr:
      res *= (a[1] + 1)
    cache[n] = res
    return res

tot = 0
for cd in range(1, N):
  ab = N - cd

  c = factorization(cd)
  c *= factorization(ab)
  tot += c

print(tot)