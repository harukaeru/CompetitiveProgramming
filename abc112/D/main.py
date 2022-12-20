#!/usr/bin/env python3.8
N, M = map(int, input().split())

# 素因数分解
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

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

facts = factorization(M)
cnts = [f[1] for f in facts]
p = 1
for c in cnts:
  p *= (c + 1)

fin = 1
for i in range(1, p):
  j = i
  ans = 1
  for pos, cnt in enumerate(cnts):
    ans *= facts[pos][0] ** (j % (cnt + 1))
    j //= (cnt + 1)
  # print('ans', ans)
  k = M // ans
  # print('K', k)
  if N <= k:
    fin = max(fin, ans)
print(fin)