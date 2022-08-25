#!/usr/bin/env python3
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []

new_A = [(A[i], -i) for i in range(N)]
new_A.sort(reverse=True)
ans += [-a[1] for a in new_A[:X]]
# print('After A', ans)

new_B = [(B[i], -i) for i in range(N) if i not in ans]
new_B.sort(reverse=True)
ans += [-b[1] for b in new_B[:Y]]
# print('After B', ans)

new_AB = [(A[i] + B[i], -i) for i in range(N) if i not in ans]
new_AB.sort(reverse=True)
ans += [-ab[1] for ab in new_AB[:Z]]
# print('After AB', ans)

for a in sorted(ans):
  print(a + 1)