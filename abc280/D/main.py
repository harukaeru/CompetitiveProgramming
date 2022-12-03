#!/usr/bin/env python3.8
import bisect
from collections import defaultdict
import math


K = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

m = 1
# print(factorization(K))
for c, k in factorization(K):
  d = 1
  cnt = 0
  for j in range(1, k + 1):
    p = j * c
    # print('p', p)
    while p % c == 0:
      cnt += 1
      p //= c
    if cnt >= k:
      break
  # print('cnt', cnt)
  # print('j', j)

  m = max(m, c * j)
print(m)