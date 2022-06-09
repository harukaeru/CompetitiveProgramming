#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int H, W;
  cin >> H >> W;

  vector<string> vec(H);
  rep(i, H) {
    cin >> vec.at(i);
  }

  vector<string> cut_rows;
  rep(i, H) {
    string row = vec.at(i);
    bool should_keep = false;
    rep(j, row.size()) {
      if (row.at(j) == '#') {
        should_keep = true;
        break;
      }
    }

    if (should_keep) {
      cut_rows.push_back(row);
    }
  }

  vector<int> keeper;
  rep(i, W) {
    bool should_keep = false;
    rep(r, cut_rows.size()) {
      string row = cut_rows.at(r);
      if (row.at(i) == '#') {
        should_keep = true;
        break;
      }
    }

    if (should_keep) {
      keeper.push_back(i);
    }
  }

  rep(i, cut_rows.size()) {
    string row = cut_rows.at(i);

    for (int j = 0; j < (int)(keeper.size()); j++) {
      int k = keeper.at(j);

      cout << row.at(k);
    }
    cout << endl;
  }

  return 0;
}
