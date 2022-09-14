A = [5, 11, 1, 8, 7, 2]

S = [0] * (len(A) + 1)
for i in range(len(A)):
  S[i + 1] = A[i] + S[i]

print(S[4] - S[1])
print(S)