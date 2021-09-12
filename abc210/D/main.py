#!/usr/bin/env python3
H, W, C = map(int, input().split())

MAX = 2 * 10 ** 12 + 2 * 10 ** 9

HW = []
for i in range(H):
    *w, = map(int, input().split())
    HW.append(w)


# minimum_cost = 999999999999999
# m2 = 999999999999999
# for i in range(H):
#     ii = i + 1
#     for j in range(W):
#         jj = j + 1
#         print('p', HW[i][j] - C * (ii + jj))
#         print('q', HW[i][j] + C * (ii + jj))
#         print('-' * 20)
#         minimum_cost = min(minimum_cost, HW[i][j] - C * (ii + jj))
#         m2 = min(m2, HW[i][j] + C * (ii + jj))
#
# print(minimum_cost)
# print(m2)
