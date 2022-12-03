#!/usr/bin/env python3.8
S = input()
T = input()

ans = None
for i in range(len(S) - len(T), -1, -1):
  ok = True
  # print('i', i)
  for j in range(len(T)):
    s = S[i + j]
    t = T[j]
    # print('   ', (s, t))
    if s == '?':
      continue
    elif s == t:
      continue

    ok = False
    break
  if ok:
    ans = S[:i] + T + S[i + len(T):]
    break

if ans is None:
  print('UNRESTORABLE')
else:
  print(ans.replace('?', 'a'))