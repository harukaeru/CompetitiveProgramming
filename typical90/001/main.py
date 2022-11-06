#!/usr/bin/env python3.8
N, L = map(int, input().split())
K = int(input())
*A, = map(int, input().split())

A = [0] + A + [L]
diffs = []
for i in range(len(A) - 1):
    diff = A[i + 1] - A[i]
    diffs.append(diff)

# print(diffs)

def can_cut(diffs, m, K):
    k = 0
    s = 0
    for a in diffs:
        s += a
        if s >= m and k < K:
            s = 0
            k += 1
    if s >= m and k == K:
        return True
    return False

def search(start, end):
    # print('start', start, end)
    if start == end:
        return start

    if end - start == 1:
        if can_cut(diffs, end, K):
            return end
        return start

    d = (end - start) // 2
    mid = start + d
    cuttable = can_cut(diffs, mid, K)
    if cuttable:
        return search(mid, end)
    else:
        return search(start, mid)


s = 1
e = 10 ** 9
print(search(s, e))
