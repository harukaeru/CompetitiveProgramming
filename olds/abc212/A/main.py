#!/usr/bin/env python3.8

A, B = map(int, input().split())

if 0 < A and 0 == B:
    print('Gold')
elif 0 == A and 0 < B:
    print('Silver')
else:
    print('Alloy')
