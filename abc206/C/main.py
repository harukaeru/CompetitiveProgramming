#!/usr/bin/env python3
from collections import Counter
N = int(input())
*A, = map(int, input().split())

counters = Counter(A)
# print('c', counters)
s = 0
for a in A:
    other_num_cases = N - counters[a]
    s += other_num_cases

print(s // 2)
