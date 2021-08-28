r, c = map(int, input().split())

s_row = [0 for x in range(c)]

for i in range(r):
    row = list(map(int, input().split()))
    s = 0
    for j in range(c):
        s += row[j]
        s_row[j] += row[j]
        print(row[j], end=' ')
    print(s)

sss = 0
for num in s_row:
    print(num, end= ' ')
    sss += num
print(sss)
