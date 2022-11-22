from collections import defaultdict
N, M = map(int, input().split())

G = defaultdict(set)
for i in range(M):
  a, b = map(int, input().split())
  G[a].add(b)
  G[b].add(a)

seen = set()
def dfs(s, prev, d):
  for nex in G[s]:
    print('(s,n)', (s, nex), ':p', prev)
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

s = list(G.keys())[0]
if dfs(s, None, d=s):
  print('close')
else:
  print('not close')
