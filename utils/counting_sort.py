A = [9, 2, 7, 3, 3, 4, 2, 7, 3, 1, 11, 10, 8, 5, 31, 2]

C = [0] * (max(A) + 1)
for a in A:
  C[a] += 1

R = []
for i, c in enumerate(C):
  for _ in range(c):
    R.append(i)

print(R)