#!/usr/bin/env python3
import bisect
from array import array

L, Q = map(int, input().split())
keys = array("i", [L])


for __ in range(Q):
    c_i, x_i = map(int, input().split())
    if c_i == 1:
        pos = bisect.bisect_left(keys, x_i)
        # bisect.insort_left(keys, x_i)
        # keys = keys[:pos] + [x_i] + keys[pos:]  # .insert(pos, x_i)
        keys.insert(pos, x_i)
        # print('keys', keys)
    else:
        pos = bisect.bisect_left(keys, x_i)
        k = keys[pos]
        if pos - 1 < 0:
            print(k - 0)
        else:
            print(k - keys[pos - 1])
