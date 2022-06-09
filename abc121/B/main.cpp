#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M, C;
  cin >> N >> M >> C;
  vector<int> B(M);
  rep(i, M) {
    cin >> B.at(i);
  }

  int cnt = 0;
  rep(i, N) {
    int t = 0;
    rep(j, M) {
      int a;
      cin >> a;
      t += a * B.at(j);
    }

    if (t + C > 0) {
      cnt++;
    }
  }

  cout << cnt << endl;
  return 0;
}
