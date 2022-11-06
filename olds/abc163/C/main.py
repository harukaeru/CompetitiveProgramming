#!/usr/bin/env python3.8

N = int(input())
*A, = map(int, input().split())

boss_counter = [0] * N

for i in range(N - 1):
    boss_counter[A[i] - 1] += 1

for b in boss_counter:
    print(b)
