#!/usr/bin/env python3.8
SATIS = 'satisfiable'

N = int(input())
A = set()
B = set()
for i in range(N):
    s = input()
    if s.startswith('!'):
        B.add(s.replace('!', ''))
    else:
        A.add(s)

s = A & B
if s:
    print(s.pop())
else:
    print(SATIS)
