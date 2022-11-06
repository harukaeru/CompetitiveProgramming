#!/usr/bin/env python3.8
N,M = map(int,input().split())
A = list(map(int,input().split()))
maxA = max(max(A),M)

k = [True] * (maxA+1) # iが条件を満たすkか(iが使えるか)
isprime = [True] * (maxA+1) # iが素数か
prime = [] # Aの素因数(使えない素数)
# Aの要素は使えない
for a in A:
    k[a] = False
# エラトステネスの篩
for i in range(2,maxA+1):
    if not isprime[i]:
        continue
    for j in range(i*2,maxA+1,i):
        isprime[j] = False
        # iはjの素因数
        # jがAの要素ならiは使えない素数
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)
print('k', k)
for i, j in enumerate(k):
    if j:
        print(i+1)
print('prime', prime)
# 使えない素数pに対して, pの倍数を使えなくする
for p in prime:
    for j in range(p*2,M+1,p):
        k[j] = k[j] and k[p]
# 使える数をansに入れる
ans = [1]
for i in range(2,M+1):
    if k[i]:
        ans.append(i)
# 出力
print(len(ans))
for i in ans:
    print(i)
