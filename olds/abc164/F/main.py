#!/usr/bin/env python3.8
import sys


def solve(N: int, S: "List[int]", T: "List[int]", U: "List[int]", V: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    U = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, T, U, V)

if __name__ == '__main__':
    main()
