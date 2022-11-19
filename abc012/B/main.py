#!/usr/bin/env python3.8
N = int(input())

ss = N % 60
tmm = N // 60
mm = tmm % 60
hh = tmm // 60

print(f'{hh:02d}:{mm:02d}:{ss:02d}')