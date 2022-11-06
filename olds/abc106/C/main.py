#!/usr/bin/env python3.8
S = input()
K = int(input())

BIG = 5000_0000_0000_0000

current_pos = 0
pos_list = [0]

limit_1 = 0
for i, s in enumerate(S):
    if s == '1':
        limit_1 += 1
    else:
        break

if K > limit_1:
    for i, s in enumerate(S):
        if s != '1':
            print(s)
            exit()
else:
    print(1)
# print(list(s))
# print(pos_list)
