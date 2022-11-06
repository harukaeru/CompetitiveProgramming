#!/usr/bin/env python3.8
N = int(input())
*A, = map(int, input().split())

half = len(A) // 2
semi_prize_rate = min(max(A[:half]), max(A[half:]))
print(A.index(semi_prize_rate) + 1)
