#!/usr/bin/env python3
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

m = min([A, B, C, D, E])

cnt = (N + m - 1) // m
# print('cnt', cnt)
print(cnt - 1 + 5)