#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, Q: int, x: "List[int]", y: "List[int]", z: "List[int]", w: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    z = [int()] * (Q)  # type: "List[int]"
    w = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, Q, x, y, z, w)

if __name__ == '__main__':
    main()
