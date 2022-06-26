#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  vector<vector<int>> vec(3);
  rep(i, 3) {
    rep(j, 3) {
      int k;
      cin >> k;
      vec.at(i).push_back(k);
    }
  }

  int N;
  cin >> N;

  rep(k, N) {
    int b;
    cin >> b;
    rep(i, 3) {
      rep(j, 3) {
        if (b == vec.at(i).at(j)) {
          vec.at(i).at(j) = -1;
        }
      }
    }
  }

  /*
  rep(i, 3) {
    rep(j, 3) {
      cout << vec.at(i).at(j) << ' ';
    }
    cout << endl;
  }
  */

  rep(i, 3) {
    bool ok = vec.at(i).at(0) == -1 && vec.at(i).at(1) == -1 && vec.at(i).at(2) == -1;
    if (ok) {
      cout << "Yes" << endl;
      return 0;
    }
  }

  rep(j, 3) {
    bool ok = vec.at(0).at(j) == -1 && vec.at(1).at(j) == -1 && vec.at(2).at(j) == -1;
    if (ok) {
      cout << "Yes" << endl;
      return 0;
    }
  }

  bool ok = (vec.at(0).at(0) == -1 && vec.at(1).at(1) == -1 && vec.at(2).at(2) == -1) || (vec.at(2).at(0) == -1 && vec.at(1).at(1) == -1 && vec.at(0).at(2) == -1);
  if (ok) {
    cout << "Yes" << endl;
    return 0;
  }
  cout << "No" << endl;
  return 0;
}
