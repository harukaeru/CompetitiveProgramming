#!/usr/bin/env python3.8
import sys


def solve(N: int, S: "List[str]", T: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        T[i] = int(next(tokens))
    solve(N, S, T)

if __name__ == '__main__':
    main()
