#!/usr/bin/env python3.8
N,M,K=map(int, input().split())
S = []
for i in range(N):
  a,b=map(int, input().split())
  S.append((a, a + b))

S.sort(key=lambda x: x[1])

T = []
for i in range(M):
  c,d=map(int, input().split())
  T.append((c, c + d))
T.sort(key=lambda x: x[1])

anses = []
for i in range(N):
  aes = []
  for j in range(M):
    aes.append((S[i][0] + T[j][0], S[i][1] + T[j][1]))
  anses.append(aes)

print('      ', T)
for s in S:
  print(s)
print('--------')
for a in anses:
  print(a)

print('--------')

data = []
for aes in anses:
  print(*[a[0]/a[1] * 100 for a in aes])
  data += [a[0]/a[1] * 100 for a in aes]
data.sort()
data.reverse()

print(data)