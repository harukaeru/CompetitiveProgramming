#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int s = abs(a - b) + abs(b - c) + abs(c - a);
  int m = max({abs(a - b), abs(b - c), abs(c - a)});

  cout << s - m << endl;
  return 0;
}
