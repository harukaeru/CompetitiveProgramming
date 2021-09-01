def modpow(a, n, mod):
    res = 1
    while n > 0:
        if (n & 1):
            res = res * a % mod

        a = a * a % mod
        n >>= 1
    return res
print(modpow(3, 3, 1000000007))
