#!/usr/bin/env python3

N, M = map(int, input().split())

switches_list = []
for __ in range(M):
    k, *s, = map(int, input().split())
    switches_list.append(s)

switch_num_list = []
for m in range(M):
    switches = switches_list[m]
    switch_num = 0
    for s in switches:
        switch_num |= 2 ** (s - 1)
    switch_num_list.append(switch_num)

*p, = map(int, input().split())


total = 0
for i in range(2 ** N):
    current_switch_state = i

    ok_count = 0
    for j, switch_num in enumerate(switch_num_list):
        count = 0
        light = bin(current_switch_state & switch_num)
        for c in light:
            if c == '1':
                count += 1
        if count % 2 == p[j]:
            ok_count += 1
        else:
            break
    if ok_count == M:
        total += 1


print(total)
