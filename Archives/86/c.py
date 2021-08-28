N = int(input())
time_array = [[0, 0, 0]]

for __ in range(N):
    time_array.append(list(map(int, input().split())))

d_time_array = []
for i in range(len(time_array) - 1):
    dt = time_array[i+1][0] - time_array[i][0]
    dx = time_array[i+1][1] - time_array[i][1]
    dy = time_array[i+1][2] - time_array[i][2]
    d_time_array.append([dt, dx, dy])

for (dt, dx, dy) in d_time_array:
    distance = abs(dx) + abs(dy)
    if distance > dt:
        print('No')
        exit()

    if distance == dt:
        continue  # ok

    rest = dt - distance
    if rest % 2 == 0:
        continue  # ok
    else:
        print('No')
        exit()
print('Yes')
