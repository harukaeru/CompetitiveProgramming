a = list(range(1000000000))
c = [0] * (len(a) + 1)

for i, v in enumerate(a):
    c[i + 1] = c[i] + v

def get_cum(start_idx, end_idx):
    print(c[end_idx] - c[start_idx])

get_cum(2, 10)

m = 0
for x in range(2, 10):
    m += a[x]
print(m)
