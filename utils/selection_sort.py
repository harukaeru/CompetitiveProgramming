A = [3, 9, 2, 5, 2, 1]

for i in range(len(A)):
  m = 99999999999
  m_j = i
  for j in range(i, len(A)):
    if m > A[j]:
      m = A[j]
      m_j = j
  A[i], A[m_j] = A[m_j], A[i]

print(A)