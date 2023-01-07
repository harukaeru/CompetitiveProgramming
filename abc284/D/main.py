#!/usr/bin/env pypy3
# 素因数分解

from math import sqrt


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
        if arr:
          break

    if arr[0][1] == 1:
      arr.append([int(sqrt(temp)), 2])
    else:
      arr.append([temp, 1])

    return arr


# def factorization2(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5 // 1)) + 1):
#         if temp % i == 0:
#             cnt = 0
#             while temp % i == 0:
#                 cnt += 1
#                 temp //= i
#             arr.append([i, cnt])
# 
#     if temp != 1:
#         arr.append([temp, 1])
# 
#     if arr == []:
#         arr.append([n, 1])
# 
#     return arr

T = int(input())
for i in range(T):
  N = int(input())

  # x = list(ans.items())
  x = factorization(N)
  # print('x', x)
  if x[0][1] == 1:
    print(x[1][0], x[0][0])
  else:
    print(x[0][0], x[1][0])