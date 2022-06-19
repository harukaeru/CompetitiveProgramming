#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int n;
  cin >> n;

  vector<int> p(n);

  rep(i, n) {
    cin >> p.at(i);
  }

  int cnt = 0;
  for (int i = 1; i < n - 1; i++) {
    if ((p.at(i - 1) < p.at(i) && p.at(i) < p.at(i + 1)) || (p.at(i + 1) < p.at(i) && p.at(i) < p.at(i - 1))) {
      cnt++;
    }
  }
  cout << cnt << endl;
  return 0;
}
