#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, T: "List[int]", X: "List[int]", Y: "List[int]", V: "List[int]"):
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
    T = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    V = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, Q, T, X, Y, V)

if __name__ == '__main__':
    main()
