A = [13, 34, 50, 75]
B = [11, 20, 28, 62]

C = []

i_a = 0
i_b = 0
while i_a < len(A) or i_b < len(B):
  if i_a == len(A):
    C.append(B[i_b])
    i_b += 1
  elif i_b == len(B):
    C.append(A[i_a])
    i_a += 1
  elif A[i_a] >= B[i_b]:
    C.append(B[i_b])
    i_b += 1
  else:
    C.append(A[i_a])
    i_a += 1
  
print(C)
