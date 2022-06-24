#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, D;
  cin >> N >> D;

  int d = D * 2 + 1;
  cout << (N + d - 1) / d << endl;

  return 0;
}
