MOD = 1000000007
a = 12345678900000
b = 100000

def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = a // b

        a -= t * b
        a, b = b, a

        u -= t * v
        u, v = v, u

    u %= m
    if (u < 0):
        u += m
    return u

a = a % MOD

print(a * modinv(b, MOD) % MOD)
