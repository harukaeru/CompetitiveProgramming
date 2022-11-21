#!/usr/bin/env python3.8
W = int(input())

ans = []
ans += list(range(1, 100))
ans += [100 * x for x in range(1, 100)]
ans += [10000 * x for x in range(1, 100)]

print(len(ans))
print(*ans) 
