#!/usr/bin/env python3
N = int(input())
*a, = map(int, input().split())

max_counter = {}

def increment(j, counter):
    counter.setdefault(j, 0)
    counter[j] += 1


for i in range(N):
    increment(a[i] + 1, max_counter)
    increment(a[i], max_counter)
    increment(a[i] - 1, max_counter)

maximum = -1

for k, v in max_counter.items():
    if v > maximum:
        maximum = v

print(maximum)
