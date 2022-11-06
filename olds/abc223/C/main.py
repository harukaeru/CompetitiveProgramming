#!/usr/bin/env python3.8
N = int(input())

L = []
t = 0
for i in range(N):
    A, B = map(int, input().split())
    L.append([A, B])
    t += A / B
# print(t)

x = t / 2
# print(x)

l = 0
for (A, B) in L:
    t = A / B
    if x <= t:
        # 決定
        l += x * B
        break
    else:
        x -= t
        l += A
print(l)
