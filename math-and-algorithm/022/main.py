#!/usr/bin/env python3
import math
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

cnt = 0
for i in range(1, 50000):
  j = 100000 - i
  cnt += counter[i] * counter[j]

cnt += math.comb(counter[50000], 2)
print(cnt)