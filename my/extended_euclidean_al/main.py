def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)

    q = a // b
    r = a % b
    d, s, t = ext_gcd(b, a % b)
    x = t
    y = s - q * t
    # print('x,y', x, y)
    # y -= a // b * x
    return d, x, y

print(tuple(ext_gcd(111, 30)[1:]))
