#!/usr/bin/env python3
N = int(input())
S = list(input())
Q = int(input())

it = 0

for i in range(Q):
    q, a, b = map(int, input().split())

    if q == 1:
        a, b = a - 1, b - 1
        a, b = (a + it) % (2 * N), (b + it) % (2 * N)
        S[a], S[b] = S[b], S[a]
    else:
        it += N
        it %= (2 * N)

# PyPy用
ans = [S[(it + i) % (2 * N)] for i in range(2 * N)]
print(''.join(ans))
