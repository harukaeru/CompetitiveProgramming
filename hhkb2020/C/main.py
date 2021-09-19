#!/usr/bin/env python3
N = int(input())
*p, = map(int, input().split())

ans = 0
ng_set = set()
for pi in p:
    ng_set.add(pi)
    while ans in ng_set:
        ans += 1
    print(ans)
