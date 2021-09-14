#!/usr/bin/env python3
N = int(input())
*T, = map(int, input().split())
# 6
# 5 4 6 7 9 10
# -> 22になってしまう

MAX = sum(T)

T.sort()
T.reverse()

# print(T)

def is_matched(ans):
    s1 = 0
    s2 = 0
    for t in T:
        if s1 + t > ans:
            s2 += t
        else:
            s1 += t
    if s1 <= ans and s2 <= ans:
        return True
    return False

left = 0
right = MAX

while right - left > 1:
    mid = left + (right - left) // 2

    if (is_matched(mid)):
        right = mid
    else:
        left = mid

# print(MAX)
print(right)
