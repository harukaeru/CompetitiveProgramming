import datetime
import math
N2 = 10 ** 7
N = int(math.sqrt(N2)) + 1
start = datetime.datetime.now()
dp = {}
for i in range(N):
    for j in range(N):
        dp[(i, j)] = 1

end = datetime.datetime.now()
print(end - start, 'tuple')

start = datetime.datetime.now()
dp = []
for i in range(N):
    dp.append([0] * N)

for i in range(N):
    for j in range(N):
        dp[i][j] = 1

end = datetime.datetime.now()
print(end - start, 'list')

