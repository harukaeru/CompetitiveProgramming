#!/usr/bin/env python3

K = int(input())

cache = {}

def gcd(a, b):
    t = (a, b)
    if cache.get(t):
        return cache[t]

    if b == 1:
        cache[t] = 1
        return 1

    c = a % b
    if c == 0:
        cache[t] = b
        return b

    ret = gcd(b, c)
    cache[t] = ret
    return ret

counter = {}

def set_counter(j):
    counter.setdefault(j, 0)
    counter[j] += 1

for a in range(1, K + 1):
    for b in range(1, K + 1):
        z = gcd(a, b)
        set_counter(z)

print('len', len(list(counter.keys())))
ans = 0
for c in range(1, K + 1):
    for z, count in counter.items():
        result = gcd(z, c)
        ans += result * count

print(ans)
