#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int K, X;
  cin >> K >> X;

  vector<int> ans;
  int d = K - 1;
  for (int i = X - d; i <= X + d; i++) {

    if (-1000000 <= i && i <= 10000000) {
      ans.push_back(i);
    }
  }

  rep(i, ans.size()) {
    cout << ans.at(i);

    if (i == (int)ans.size() - 1) {
      cout << endl;
    } else {
      cout << ' ';
    }
  }

  return 0;
}
