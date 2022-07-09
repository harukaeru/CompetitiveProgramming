#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, K;
  cin >> N >> K;

  vector<int> counter(N);
  rep(k, K) {
    int d_i;
    cin >> d_i;

    rep(j, d_i) {
      int a;
      cin >> a;
      a--;
      counter.at(a)++;
    }
  }

  int ans = 0;
  for (auto c : counter) {
    if (c < 1) {
      ans++;
    }
  }
  cout << ans << endl;
  return 0;
}
