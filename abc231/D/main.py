#!/usr/bin/env python3.8
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(1000000)


N, M = map(int, input().split())
if M == 0:
  print('Yes')
  exit()

G = defaultdict(set)
for i in range(M):
  a, b = map(int, input().split())
  G[a].add(b)
  G[b].add(a)

for v in G.values():
  if len(v) >= 3:
    print('No')
    exit()

seen = set()
def dfs(s, prev, d):
  for nex in G[s]:
    if nex == prev:
      continue
    if nex == d:
      return True
    if nex not in seen:
      seen.add(nex)
      ans = dfs(nex, s, d)
      if ans:
        return ans

  return False

# visited = [False] * (N+1)
# stack = list()
# try:
#   for i in range(1,N+1):
#       if visited[i] == True:continue
#       stack.append((-1,i))
#       visited[i] = True
#       while len(stack) != 0:
#           par,pos = stack.pop()
#           for nex in G[pos]:
#               if par != nex:
#                   if visited[nex] == False:
#                       visited[nex] = True
#                       stack.append((pos,nex))
#                   else:
#                       print(pos, G[pos])
#                       print(nex, G[nex])
#                       print(1, G[1])
#                       print('No')
#                       raise Exception()
# except:
#   pass

for i in range(1, N + 1):
  if dfs(i, None, d=i):
    print('No')
    exit()
print('Yes')