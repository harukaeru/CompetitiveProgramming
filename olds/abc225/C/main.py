#!/usr/bin/env python3.8

N, M = map(int, input().split())

bb = []
for i in range(N):
    *b, = map(int, input().split())
    bb.append(b)

co = len(bb[0])
initial = bb[0][0]
c = initial % 7
if c == 0:
    c = 7

if c + co > 8:
    print('No')
    exit()

for i, b in enumerate(bb):
    addition = i * 7
    h = initial + addition
    for j, x in enumerate(b):
        if x != (h + j):
            print('No')
            exit()

print('Yes')
