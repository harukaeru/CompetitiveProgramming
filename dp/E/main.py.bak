#!/usr/bin/env python3
N, W = map(int, input().split())
wv = []
for __ in range(N):
    w, v = map(int, input().split())
    wv.append([w, v])

INF = 999999999
maximum_value = sum([x[1] for x in wv])

dp = [[INF for i in range(maximum_value + 1)] for __ in range(N + 1)]
dp[0][0] = 0

for i, (w, v) in enumerate(wv):
    for j in range( maximum_value + 1):
        prev_idx = max(j - v, 0)
        dp[i + 1][j] = min(dp[i][prev_idx] + w, dp[i][j])

# print('maximum_value', maximum_value)
max_j = 0
for j, cw in enumerate(dp[-1]):
    # print('j', j)
    # print('cw', cw)
    if W >= cw:
        max_j = max(j, max_j)


# for i, d in enumerate(dp):
#     print(i, '-------------------')
#     print(*d)
# # from pprint import pprint
# # pprint(dp)
# import bisect
# print(bisect.bisect_right(dp[-1], W) - 1)
print(max_j)
