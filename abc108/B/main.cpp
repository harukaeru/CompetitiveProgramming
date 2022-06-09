#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;

  int dx = x2 - x1;
  int dy = y2 - y1;

  cout << x2 - dy << ' ';
  cout << y2 + dx << ' ';
  cout << (x2 - dy) - dx << ' ';
  cout << (y2 + dx) - dy;
  cout << endl;

  return 0;
}
