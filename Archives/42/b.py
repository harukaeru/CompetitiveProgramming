N, L = map(int, input().split())

l = []
for i in range(N):
    l.append(input().replace('\n', ''))

while 1:
    change = False

    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if l[i] > l[i+1]:
                l[i+1], l[i] = l[i], l[i+1]
                change = True
    if not change:
        break
print(''.join(l))
