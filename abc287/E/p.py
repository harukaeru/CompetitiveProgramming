N = 250000
print(N)

for i in range(N):
    x = chr(ord('a') + i % 26)
    print(x + 'p')

