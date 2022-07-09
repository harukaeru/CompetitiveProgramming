#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long long o = 1e18;
  int N;
  cin >> N;

  vector<long long> A(N);
  rep(i, N) {
    cin >> A.at(i);
    if (A.at(i) == 0) {
      cout << 0 << endl;
      return 0;
    }
  }

  long long ans = 1;
  rep(i, N) {
    long long a = A.at(i);
    if (o / ans >= a) {
      ans *= a;
    } else {
      cout << -1 << endl;
      return 0;
    }
  }

  cout << ans << endl;
  return 0;
}
