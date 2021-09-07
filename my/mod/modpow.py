def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

def modinv2(a, mod):
    return modpow(a, mod - 2, mod)

def modinv(a, mod):
    b = mod
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
        print('t', t)
        print('a, b', a, b)
        print('u', u)
        print('v', v)
        print('-'*20)
    u %= mod
    if (u < 0):
        u += mod
    return u


print(11, ':', modinv(11, 13))
# for i in range(1, 12):
#     print(i, ':', modinv(i, 13))
