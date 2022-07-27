#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int H, W;
  cin >> H >> W;

  vector<int> values;
  int min_v = 999999999;
  rep(i, H) {
    rep(j, W) {
      int k;
      cin >> k;
      values.push_back(k);
      min_v = min(min_v, k);
    }
  }

  int ans = 0;
  for (auto v : values) {
    ans += v - min_v;
  }

  cout << ans << endl;

  return 0;
}
