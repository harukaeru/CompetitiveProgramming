N, K = map(int, input().split())
*D, = input().split()

def includes_hates(num):
    for i in str(num):
        if i in D:
            return True
    return False

while 1:
    if includes_hates(N):
        N += 1
    else:
        print(N)
        break
