N, K, M = map(int, input().split())
*A, = map(int, input().split())

s = 0
for a in A:
    s += a

last_score = M * N - s
if last_score <= 0:
    print(0)
elif last_score > K:
    print(-1)
else:
    print(last_score)
