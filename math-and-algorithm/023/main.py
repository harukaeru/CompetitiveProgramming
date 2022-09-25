#!/usr/bin/env python3
N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

print(sum(B) / len(B) + sum(R) / len(R))