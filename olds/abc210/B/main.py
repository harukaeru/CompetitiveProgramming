#!/usr/bin/env python3.8
N = int(input())
S = input()

s = S.index('1')

if s % 2 == 0:
    print('Takahashi')
else:
    print('Aoki')
