A = int(input()) + 1
B = int(input()) + 1
C = int(input()) + 1
X = int(input())

count = 0

for a in range(A):
    for b in range(B):
        c50 = X - (a * 500 + b * 100)
        if (c50 % 50 == 0) and (0 <= (c50 / 50) < C):
            count += 1

print(count)
