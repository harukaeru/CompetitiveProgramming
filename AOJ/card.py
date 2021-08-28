import sys

length = sys.stdin.readline()

set_list = [set(range(1, 14)) for n in range(4)]

def get_num_set(symbol):
    if symbol == 'S':
        return set_list[0]
    if symbol == 'H':
        return set_list[1]
    if symbol == 'C':
        return set_list[2]
    if symbol == 'D':
        return set_list[3]

for line in sys.stdin:
    symbol, num = line.replace('\n', '').split(' ')
    num = int(num)
    num_set = get_num_set(symbol)
    num_set.remove(num)

for symbol in ['S', 'H', 'C', 'D']:
    num_list = sorted(get_num_set(symbol))
    for num in num_list:
        print(symbol, num)
