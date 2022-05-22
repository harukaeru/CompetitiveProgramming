#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int a, b;
  cin >> a >> b;
  int d = b - a;

  cout << d * (d + 1) / 2 - b << endl;
  return 0;
}
