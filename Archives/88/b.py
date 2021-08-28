N = int(input())
*a, = map(int, input().split())

a.sort()
a.reverse()

alice = 0
bob = 0

for i in range(0, N, 2):
    alice += a[i]
    try:
        bob += a[i+1]
    except:
        pass

print(alice - bob)
