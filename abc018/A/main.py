#!/usr/bin/env python3.8
A = int(input())
B = int(input())
C = int(input())

o = [A, B, C]
o.sort()
o.reverse()

print(o.index(A) + 1)
print(o.index(B) + 1)
print(o.index(C) + 1)