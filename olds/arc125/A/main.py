#!/usr/bin/env python3.8
N, M = input().split()
*S, = map(int, input().split())
*T, = map(int, input().split())

set_t = set(T)

if len(set_t) == 1:
    # Tの種類が1個 かつ 動かす必要がない
    if set([S[0]]) == set_t:
        print(len(T))
        exit()
    # Tの種類が1個 かつ Sにそれが存在しない
    if T[0] not in set(S):
        print(-1)
        exit()

# Tの種類は複数あるが、Sの種類が複数ない
if len(set_t) > 1:
    if set(S) != set_t:
        print('-1')
        exit()

num_to_search = S[0] ^ 1

left_min = S.index(num_to_search)
reversed_S = list(reversed(S))
right_min = reversed_S.index(num_to_search) + 1

# print('T', T)
# print('left', left_min)
# print('right', right_min)
min_num_to_dial = min(left_min, right_min)

current = S[0]
count = 0
is_first_dial = True
for t in T:
    if t == current:
        count += 1
        continue
    elif t != current:
        current = t
        if is_first_dial:
            is_first_dial = False
            count += min_num_to_dial
        else:
            count += 1
        count += 1

print(count)
