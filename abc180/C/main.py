#!/usr/bin/env python3
import math
N = int(input())

ans = set()
for a in range(1, int(math.sqrt(N)) + 1):
    if (N % a) == 0:
        ans.add(a)
        ans.add(N // a)

ans = list(ans)
ans.sort()
for a in ans:
    print(a)
