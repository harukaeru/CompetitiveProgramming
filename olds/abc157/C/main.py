#!/usr/bin/env python3
N, M = map(int, input().split())

collations = {}
for i in range(M):
    s_i, c_i = map(int, input().split())
    c_i = str(c_i)

    if collations.get(s_i):
        if collations[s_i] != c_i:
            print(-1)
            exit()

    collations[s_i] = c_i

start = 0 if N == 1 else 10 ** (N - 1)
for n in range(start, 10 ** N + 1):
    sn = str(n)

    is_matched = True
    for s_i, c_i in collations.items():
        try:
            l = sn[s_i - 1]
            if l != c_i:
                is_matched = False
        except:
            is_matched = False
    if is_matched:
        print(n)
        exit()

print(-1)
