#!/usr/bin/env python3
from collections import defaultdict

N, K = map(int, input().split())
moneys = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    moneys[a] += b

city_nums = sorted(moneys.keys())

m = K
for city in city_nums:
    if city > m:
        break
    else:
        m += moneys[city]

print(m)
