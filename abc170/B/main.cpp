#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int X, Y;
  cin >> X >> Y;

  for (int a = 0; a <= 100; a++) {
    for (int b = 0; b <= 100; b++) {
      if ((X == a + b) && (Y == 2 * a + 4 * b)) {
        cout << "Yes" << endl;
        return 0;
      }
    }
  }

  cout << "No" << endl;
  return 0;
}
