#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int X;
  cin >> X;

  int max_500 = X / 500;
  int max_5 = (X % 500) / 5;

  cout << max_500 * 1000 + max_5 * 5 << endl;
  return 0;
}
