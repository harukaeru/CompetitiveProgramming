#!/usr/bin/env python3.8
H, W = map(int, input().split())

array = []
for __ in range(H):
    array.append(input())


def check(array, ii, jj):
    try:
        a = array[ii][jj]
        if a == '#':
            return True
    except:
        pass
    return False

# print('array', array)
for i in range(H):
    for j in range(W):
        if array[i][j] == '#':
            can_fill = False
            can_fill = can_fill or check(array, i + 1, j)
            can_fill = can_fill or check(array, i - 1, j)
            can_fill = can_fill or check(array, i, j + 1)
            can_fill = can_fill or check(array, i, j - 1)
            if not can_fill:
                print('No')
                exit()
print('Yes')
