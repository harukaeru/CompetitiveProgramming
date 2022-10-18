N = 34912
S = str(N)
dlen = len(S)

dp = []
for i in range(dlen):
  d = [0, 0]
  dp.append(d)

cnt = 0
for i in range(5):
  c = ord(S[i]) - ord('0')
  print('c', c)
  dp[i][True] = c * 10 ** (dlen - (i + 1))
  dp[i][False] = 0

for d in dp:
  print('----')
  print(d)
print('cnt', cnt)