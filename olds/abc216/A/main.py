#!/usr/bin/env python3

X, Y = input().split('.')

Y = int(Y)

if 0 <= Y <= 2:
    print(X + '-')
elif 3 <= Y <= 6:
    print(X)
elif 7 <= Y <= 9:
    print(X + '+')


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    pass

if __name__ == '__main__':
    main()
