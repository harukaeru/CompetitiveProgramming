#!/usr/bin/env python3.8
import sys


def solve(N: int, C: int, x: "List[int]", v: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, C, x, v)

if __name__ == '__main__':
    main()
