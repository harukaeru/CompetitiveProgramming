x = list(range(10))
y = list(range(11))

def rev(a):
    l = len(a) // 2
    i = 0
    m = len(a) - 1
    while l > 0:
        a[i], a[m - i] = a[m - i], a[i]
        i += 1
        l -= 1
    return a

print(rev(x))
print(rev(y))
