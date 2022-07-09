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

  long d2 = (long)D * D;

  int cnt = 0;
  rep(i, N) {
    long x, y;
    cin >> x >> y;
    if (x * x + y * y <= d2) {
      cnt++;
    }
  }

  cout << cnt << endl;

  return 0;
}
