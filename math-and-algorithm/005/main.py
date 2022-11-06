#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
print(sum(A) % 100)