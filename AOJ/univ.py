import sys

columns = [
  [
    [
      0  for r_i in range(10)
    ]
    for f_i in range(3)
  ]
  for b_i in range(4)
]

row_num = int(sys.stdin.readline().replace('\n', ''))

for line in sys.stdin:
    b, f, r, v = [int(n) for n in line.replace('\n', '').split(' ')]
    columns[b - 1][f - 1][r - 1] += v

for i, building in enumerate(columns):
    for floor in building:
        for room in floor:
            print('', end=' ')
            print(room, end='')
        print()
    if i != len(columns) - 1:
        print('#'*20)

