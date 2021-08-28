#!/usr/bin/env python3

N = int(input())
S = input().replace('\n', '')

count = 0
for i in range(0, 10):
    try:
        s_i = S.index(str(i))
    except:
        continue
    for j in range(0, 10):
        try:
            s_j = S[s_i + 1:].index(str(j)) + s_i + 1
        except:
            continue
        for k in range(0, 10):
            try:
                S[s_j + 1:].index(str(k))
            except:
                continue
            count += 1

print(count)
