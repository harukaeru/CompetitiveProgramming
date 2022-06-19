#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int r, D, x_2000;
  cin >> r >> D >> x_2000;

  vector<int> ans;
  ans.push_back(x_2000);
  for (int i = 0; i < 10; i++) {
    ans.push_back(r * ans[i] - D);
  }

  for (int i = 1; i < (int)ans.size(); i++) {
    cout << ans.at(i) << endl;
  }
  return 0;
}
