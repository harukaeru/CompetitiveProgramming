A = [
  [0,0,0,0,0,0,0,0,1,0,],
  [0,1,0,0,0,0,0,0,1,1,],
  [0,1,1,0,0,0,0,0,0,0,],
  [0,0,0,0,0,1,1,1,0,0,],
  [0,0,0,0,0,0,0,0,0,0,],
  [0,0,0,0,0,0,0,1,0,0,],
  [0,0,0,0,0,0,0,1,0,0,],
]

seen = set()

def dfs(pos):
  y, x = pos
  seen.add((y, x))
  if A[y][x] == 0:
    return 0

  for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]:
      if dx == 0 and dy == 0:
        continue
      ny = y + dy
      if ny < 0 or len(A) <= ny:
        continue
      nx = x + dx
      if nx < 0 or len(A[0]) <= nx:
        continue
      if (ny, nx) not in seen:
        dfs((ny, nx))
  return 1

cnt = 0
for i in range(len(A)):
  for j in range(len(A[0])):
    if (i, j) not in seen:
      cnt += dfs((i, j))
print(cnt)