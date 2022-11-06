#!/usr/bin/env python3.8

H, W = map(int, input().split())

C = []

for i in range(H):
    C.append(list(input()))

from pprint import pprint
pprint(C)
