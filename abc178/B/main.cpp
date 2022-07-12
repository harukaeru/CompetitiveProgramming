#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long a, b, c, d;
  cin >> a >> b >> c >> d;
  cout << max(max(a * c, a * d), max(b * c, b * d)) << endl;

  return 0;
}
