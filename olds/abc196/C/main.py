#!/usr/bin/env python3.8
N = int(input())

M = len(str(N)) // 2 + 1

count = 0
for i in range(1, 10 ** M):
    if int(str(i) + str(i)) <= N:
        count += 1
print(count)
