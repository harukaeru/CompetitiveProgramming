#!/usr/bin/env python3.8
N = int(input())
x = list(map(int, input().split()))
 
 
MOD = 10**9+7
def mod_inverse(n, mod):
    return pow(n, mod-2, mod)
 
# a_i = (N-1)!*(1/1+1/2+...+1/i)として、
# a_1*(x_1-x_0) + ... を計算すればよい
 
fact = 1
for i in range(N-1):
    fact = (fact*(i+1))%MOD
#print(fact)
 
a = [0]
for i in range(N-1):
    last_a = a[-1]
    a.append((last_a + fact*mod_inverse(i+1,MOD))%MOD)
 
ans = 0
for i in range(N-1):
    ans = (ans + a[i+1]*(x[i+1]-x[i])) % MOD
 
print(ans)