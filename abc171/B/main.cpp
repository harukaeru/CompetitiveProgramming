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

  vector<int> p(N);
  rep(i, N) {
    cin >> p.at(i);
  }

  sort(p.begin(), p.end());

  int ans = 0;
  rep(i, K) {
    ans += p.at(i);
  }
  cout << ans << endl;
  return 0;
}
