#!/usr/bin/env python3
N, K = map(int, input().split())
*A, = map(int, input().split())

############
# from queue import PriorityQueue
#
# maxA = max(A)
#
# q = PriorityQueue()
# for a in A:
#     key = maxA - a
#     q.put((key, a))
#
# s = 0
# for k in range(K):
#     if not q.empty():
#         maximum = q.get()
#         key, a = maximum
#         if a == 0:
#             break
#         s += a
#         a -= 1
#         key = maxA - a
#         q.put((key, a))
#     else:
#         break
#
# c_ans = s
###############

def sum_a(num):
    if num % 2 == 0:
        return (num // 2) * (num + 1)
    else:
        return num * ((num + 1) // 2)

B = []
for a in A:
    B.append(sum_a(a))

maxA = sum(A)
if K >= maxA:
    print(sum(B))
    exit()

# m以上の個数をすべて選んだときにK以下になる
def is_ok(m):
    count = 0
    for a in A:
        if a >= m:
            count += a - m + 1
    if count <= K:
        return True
    return False


left = -1
right = 2 * (10 ** 9) + 1

while right - left > 1:
    mid = left + (right - left) // 2
    if is_ok(mid):
        right = mid
    else:
        left = mid

def diffsum(x, y):
    return (y - x + 1) * (x + y) // 2

rest = K
m = right
ans = 0
for a in A:
    if a >= m:
        c = a - m + 1
        rest -= c
        ans += diffsum(m, a)
# print('#ans', ans)
# print('#rest', rest)
ans += rest * (m - 1)
# if c_ans != ans:
#     print('c_ans:', c_ans)
#     print('ans', ans)
print(ans)
# print(ans)
