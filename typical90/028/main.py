#!/usr/bin/env python3
import sys


def solve(N: int, lx: "List[int]", ly: "List[int]", rx: "List[int]", ry: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    lx = [int()] * (N)  # type: "List[int]"
    ly = [int()] * (N)  # type: "List[int]"
    rx = [int()] * (N)  # type: "List[int]"
    ry = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        lx[i] = int(next(tokens))
        ly[i] = int(next(tokens))
        rx[i] = int(next(tokens))
        ry[i] = int(next(tokens))
    solve(N, lx, ly, rx, ry)

if __name__ == '__main__':
    main()
