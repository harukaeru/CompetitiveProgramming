#!/usr/bin/env python3.8
import sys


def solve(N: int, T: int, t: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, t)

if __name__ == '__main__':
    main()
