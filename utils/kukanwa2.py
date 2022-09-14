A = [
  [1, 2, 3, 4],
  [1, 2, 3, 4],
  [1, 2, 3, 4],
  [1, 2, 3, 4],
]

s1, s2 = (1, 1)
e1, e2 = (2, 2)

S = []
for i in range(len(A) + 1):
  s = []
  for j in range(len(A[0]) + 1):
    s.append(0)
  S.append(s)

for i in range(len(A)):
  for j in range(len(A[0])):
    S[i + 1][j + 1] = A[i][j] + S[i + 1][j] + S[i][j + 1] - S[i][j]

from pprint import pprint
pprint(S)

def query(s, e):
  s1, s2 = s
  e1, e2 = e
  return S[e1][e2] - S[e1][s1] - S[s2][e2] + S[s1][s2]

print('ANS:', S[3][3] - (S[1][3] + S[3][1]) + S[1][1])
print('Query:', query((1, 1), (3, 3)))