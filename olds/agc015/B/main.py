#!/usr/bin/env python3
S = input()

ceil = len(S) - 1

count = 0
for i, s in enumerate(S):
    if s == 'U':
        # print('U', i, i * 2, ceil - i)
        count += i * 2 + (ceil - i)
    elif s == 'D':
        # print('D', i, i, (floor_count - i) * 2)
        count += i + (ceil - i) * 2
print(count)
