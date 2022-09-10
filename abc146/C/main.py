#!/usr/bin/env python3
A, B, X = map(int, input().split())

ng = 10 ** 9 + 1
ok = 0
while ng - ok > 1:
  mid = (ng + ok) // 2

  is_ok = A * mid + B * len(str(mid)) <= X
  if is_ok:
    ok = mid
  else:
    ng = mid

print(ok)