#!/usr/bin/env python3.8
A, B = map(int, input().split())

for i in range(1, 100 * 10 + 1):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        exit()

print(-1)
