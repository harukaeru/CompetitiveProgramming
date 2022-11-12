#!/usr/bin/env python3.8
N, X = map(int, input().split())
P = list(map(int, input().split()))

print(P.index(X) + 1)