A = []

def dfs():
  if len(A) == 3:
    print(A)
    return

  s = A[-1] if len(A) > 0 else 0
  for i in range(s, 3):
    A.append(i)
    dfs()
    A.pop()

dfs()