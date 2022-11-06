#!/usr/bin/env python3.8
N, K = map(int, input().split())
*A, = map(int, input().split())

cnt = len(set(A)) - K

if cnt <= 0:
    print(0)
    exit()

rest = {}
for a in A:
    if rest.get(a) is None:
        rest[a] = 1
    else:
        rest[a] += 1

s = sorted(rest.values())

ans = 0
pointer = 0
for i in range(cnt):
    ans += s[pointer]
    i += s[pointer]
    pointer += 1

print(ans)
