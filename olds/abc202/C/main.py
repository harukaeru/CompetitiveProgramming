#!/usr/bin/env python3
from collections import Counter
N = int(input())
*A, = map(int, input().split())
*B, = map(int, input().split())
*C, = map(int, input().split())

# counter = Counter(C)
# counter = Counter(B)
counter = {}

for i in range(N):
    b = B[i]
    if not counter.get(b):
        counter[b] = {
            "count": 0,
            "indexes": [],
        }
    counter[b]["count"] += 1
    counter[b]["indexes"].append(i)

C = [i - 1 for i in C]
ccounter = Counter(C)

cache = {}

t = 0
for i in range(N):
    a = A[i]
    if cache.get(a):
        t += cache[a]
        continue

    counter_b = counter.get(a)
    if counter_b:
        s = 0
        for j in counter_b["indexes"]:
            if not ccounter.get(j):
                continue

            count = ccounter[j]
            s += count
        cache[a] = s
        t += s

print(t)
