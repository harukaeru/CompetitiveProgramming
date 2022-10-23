N = 10
cnt = 0
A = [2, 3, 5, 7]
Q = 1 << A[0]
for a in A[1:]:
  Q |= 1 << a

print(bin(Q))

p = Q
for k in range(1 << len(A)):
  print('p', '{:010b}'.format(p))
  # print('o', '{:010b}'.format(p-1))
  a = []
  for j in range(N):
    if p & (1 << j) != 0:
      a.append(j)
  # print(a)
  p = (p - 1) & Q
  cnt += 1

print('cnt', cnt)
