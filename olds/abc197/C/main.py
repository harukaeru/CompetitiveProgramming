#!/usr/bin/env python3.8
N = int(input())
*A, = map(int, input().split())


ans = 9999999999999999999999

# 00000110001101001010
for i in range(2 ** N):
    # print(bin(i))
    ored = 0
    xored = 0
    for j in range(N + 1):
        if (j < N):
            ored |= A[j]
        # print('ored', ored)

        if (j == N) or (i >> j & 1):
            xored ^= ored
            ored = 0
    if ans > xored:
        # print('xored', xored)
        ans = xored

print(ans)
