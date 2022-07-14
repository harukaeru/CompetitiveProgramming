#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int sx, sy, gx, gy;
  cin >> sx >> sy >> gx >> gy;

  cout << setprecision(10) << (double)sx + (double)(gx - sx) / (gy + sy) * sy << endl;

  return 0;
}
