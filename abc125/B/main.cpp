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
  vector<int> v(N);
  vector<int> c(N);

  rep(i, N) {
    cin >> v.at(i);
  }
  rep(i, N) {
    cin >> c.at(i);
  }

  int t = 0;
  rep(i, N) {
    int k = v.at(i) - c.at(i);
    if (k > 0) {
      t += k;
    }
  }

  cout << t << endl;

  return 0;
}
