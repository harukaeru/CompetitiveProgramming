#!/usr/bin/env python3.8
N = int(input())

spells = []
while N > 0:
    # print('N', N)
    if N % 2 == 0:
        N = N // 2
        spells.append('B')
    else:
        N = N - 1
        spells.append('A')

spells.reverse()
print(''.join(spells))
