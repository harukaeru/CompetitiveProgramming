#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))
print(max(A) - min(A))