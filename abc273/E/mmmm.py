Q = 5 * (10 ** 5)
print(Q)
for i in range(Q // 4):
    print('ADD', 10000)

for i in range(Q // 4):
    print('SAVE', i + 1)

for i in range(Q // 4):
    print('LOAD', i + 1)

for i in range(Q // 4):
    print('DELETE')

