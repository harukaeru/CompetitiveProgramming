#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, T;
  cin >> N >> T;

  int minc = 999999999;

  rep(i, N) {
    int c, t;
    cin >> c >> t;
    if (t <= T) {
      minc = min(minc, c);
    }
  }

  if (minc == 999999999) {
    cout << "TLE" << endl;
  } else {
    cout << minc << endl;
  }
  return 0;
}
