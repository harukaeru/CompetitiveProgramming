#include <bits/stdc++.h>
using namespace std;
#define rep(i, N) for (int i = 0; i < (int)N; i++)

int main() {
  int H, W;
  cin >> H >> W;

  vector<string> board(H);

  rep(i, H) {
    cin >> board.at(i);
  }

  vector<bool> retention_rows(H, false);
  vector<bool> retention_columns(W, false);

  rep(i, H) {
    rep(j, W) {
      if (board.at(i).at(j) == '#') {
        retention_rows.at(i) = true;
        retention_columns.at(j) = true;
      };
    }
  }

  rep(i, H) {
    if (retention_rows.at(i)) {
      rep(j, W) {
        if (retention_columns.at(j)) {
          cout << board.at(i).at(j);
        }
      }
      cout << endl;
    }
  }
}