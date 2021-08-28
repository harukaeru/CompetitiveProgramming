from enum import Enum

class Comp(Enum):
    LEFT_IS_BIGGER = 1
    SAME = 0
    LEFT_IS_SMALLER = -1

def comp_str(a, b):
    if len(a) >= len(b):
        min_len = len(b)
    else:
        min_len = len(a)

    for i in range(min_len):
        a_idx = ord(a[i])
        b_idx = ord(b[i])
        if a_idx > b_idx:
            return Comp.LEFT_IS_BIGGER
        elif a_idx < b_idx:
            return Comp.LEFT_IS_SMALLER
        elif a_idx == b_idx:
            if i == min_len - 1:
                if len(a) == len(b):
                    return Comp.SAME
                elif len(a) > len(b):
                    return Comp.LEFT_IS_BIGGER
                elif len(a) < len(b):
                    return Comp.LEFT_IS_SMALLER


tarou = 0
hanako = 0

n = int(input())

for i in range(n):
    a, b = input().replace('\n', '').split()
    compared_result = comp_str(a, b)

    if compared_result == Comp.LEFT_IS_BIGGER:
        tarou += 3
    elif compared_result == Comp.SAME:
        tarou += 1
        hanako += 1
    elif compared_result == Comp.LEFT_IS_SMALLER:
        hanako += 3

print(tarou, hanako)

