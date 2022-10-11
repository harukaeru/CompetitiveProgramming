A = [
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]

seen = []
for a in A:
  s = [False] * len(a)
  seen.append(s)

def dfs(pos):
  if seen[pos[0]][pos[1]]:
    return 0

  seen[pos[0]][pos[1]] = True
  if not A[pos[0]][pos[1]]:
    return 0

  for di in (-1, 0, 1):
    for dj in (-1, 0, 1):
      if di == 0 and dj == 0:
        continue
      ni = pos[0] + di
      nj = pos[1] + dj

      if ni < 0 or len(A) <= ni:
        continue
      if nj < 0 or len(A[0]) <= nj:
        continue

      if seen[ni][nj]:
        continue
      dfs((ni, nj))
  # print(pos)
  # A[pos[0]][pos[1]] = 2
  return 1

cnt = 0
for i in range(len(A)):
  for j in range(len(A[0])):
    cnt += dfs((i, j))

print(cnt)
for a in A:
  print(a)