#!/usr/bin/env python3
from collections import defaultdict
N, C = map(int, input().split())

date_fee_table = defaultdict(int)

for i in range(N):
    a, b, c = map(int, input().split())
    date_fee_table[a] += c
    date_fee_table[b + 1] -= c

event_dates = list(sorted(date_fee_table.keys()))

# print('ev', event_dates)

total_fee = 0
current_fee = 0
for i in range(len(event_dates) - 1):
    delta = event_dates[i + 1] - event_dates[i]
    current_fee += date_fee_table[event_dates[i]]
    total_fee += min(current_fee, C) * delta

print(total_fee)
