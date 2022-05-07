#!/usr/bin/env python3
a = [input(), input(), input(), input()]
b = ['H', '2B', '3B', 'HR']
a.sort()
b.sort()

if a == b:
    print('Yes')
else:
    print('No')
