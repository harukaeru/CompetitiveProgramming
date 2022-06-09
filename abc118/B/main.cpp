#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M;
  cin >> N >> M;

  vector<int> counter(M + 1);

  rep(i, N) {
    int k;
    cin >> k;

    rep(j, k) {
      int a;
      cin >> a;
      counter.at(a)++;
    }
  }

  int all_ok = 0;
  rep(i, counter.size()) {
    if (counter.at(i) == N) {
      all_ok++;
    }
  }

  cout << all_ok << endl;
  return 0;
}
