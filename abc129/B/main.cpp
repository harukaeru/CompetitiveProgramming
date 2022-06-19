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

  vector<int> w(N);
  int total = 0;
  rep(i, N) {
    cin >> w.at(i);
    total += w.at(i);
  }

  int s = 0;
  int min_w = 99999999;
  for (int i = 0; i < N - 1; i++) {
    s += w.at(i);

    min_w = min(min_w, abs(s - (total - s)));
  }

  cout << min_w << endl;
  return 0;
}
