#!/usr/bin/env python3.8
from itertools import combinations, permutations
N = int(input())

num = str(N)
order = range(len(num))
sorder = set(order)

d = dict(zip(order, num))

maximum = -1
for i in range(1, len(num)):
    for pa in combinations(order, i):
        pb = sorder - set(pa)
        # print(pa, pb)
        xa = []
        xb = []
        for a in pa:
            xa.append(d[a])
        for b in pb:
            xb.append(d[b])

        pxa = permutations(xa)
        pxb = permutations(xb)
        pxa = [''.join(i) for i in pxa]
        pxb = [''.join(i) for i in pxb]
        for xxa in pxa:
            if xxa.startswith('0'):
                continue
            xxa = int(xxa)
            for xxb in pxb:
                if xxb.startswith('0'):
                    continue
                xxb = int(xxb)
                maximum = max(maximum, xxa * xxb)
print(maximum)
