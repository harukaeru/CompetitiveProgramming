#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N;
  cin >> N;
  int T, A;
  cin >> T >> A;

  double min_d = 99999999;
  int found_i = -1;

  rep(i, N) {
    int h;
    cin >> h;

    double t = T - h * 0.006;
    double d = abs(A - t);
    if (min_d > d) {
      min_d = d;
      found_i = i;
    }
  }

  cout << found_i + 1 << endl;
  return 0;
}
