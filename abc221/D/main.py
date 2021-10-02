#!/usr/bin/env python3
from collections import defaultdict
N = int(input())
counters = defaultdict(int)

for i in range(N):
    A, B = map(int, input().split())
    counters[A] += 1
    counters[A + B] -= 1

# print(counters)
date_keys = sorted(counters.keys())
people_counters = [0] * (len(date_keys) + 1)

for i, date in enumerate(date_keys):
    people_counters[i + 1] = people_counters[i] + counters[date]
# print('d', [0] + date_keys)
# print('p', people_counters)

date_keys = [0] + date_keys

k_counters = defaultdict(int)

for i in range(len(people_counters) - 1):
    p = people_counters[i]
    count = date_keys[i + 1] - date_keys[i]
    k_counters[p] += count

for j in range(1, N + 1):
    print(k_counters[j], end=' ')
