#!/usr/bin/env python3.8
N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
H.reverse()

H = H[K:]

print(sum(H))