N = 200000
C = 1073741824
print(N, C)
for i in range(N):
    if i % 3 == 0:
        print(1, C - 1)
    elif i % 3 == 1:
        print(2, C - 2)
    else:
        print(3, C - 3)
