#!/usr/bin/env python3.8
from collections import Counter
import bisect
N = int(input())
A = list(map(int, input().split()))

A.sort()
counter = Counter(A)
S = list(sorted(set(A)))

m = 0
for j in range(len(S)):
  l_cnt = bisect.bisect_left(A, S[j])
  r_cnt = N - bisect.bisect_right(A, S[j])
  m += l_cnt * r_cnt * counter[S[j]]

print(m)
