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
  vector<pair<int, int>> a(N);

  rep(i, N) {
    int x, y;
    cin >> x >> y;
    a.at(i) = make_pair(x, y);
  }

  int cnt = 0;
  for (int i = 0; i < N - 1; i++) {
    auto left = a.at(i);
    for (int j = i + 1; j < N; j++) {
      auto right = a.at(j);

      double slope = (double)(right.second - left.second) / (right.first - left.first);
      if (-1 <= slope && slope <= 1) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
  return 0;
}
