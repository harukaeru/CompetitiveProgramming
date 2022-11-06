#!/usr/bin/env python3.8
R, C = map(int, input().split())
a = []
a_1 = list(map(int, input().split()))
a_2 = list(map(int, input().split()))
a.append(a_1)
a.append(a_2)

print(a[R-1][C-1])