#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  int N;
  cin >> N;

  vector<vector<vector<char>>> series_of_tik_tak_toe(N, vector<vector<char>>(3, vector<char>(3)));

  rep(t, N) {
    rep(i, 3) {
      rep(j, 3) {
        cin >> series_of_tik_tak_toe.at(t).at(i).at(j);
      }
    }
  }

  int cnt = 0;

  rep(t, N) {
    rep(i, 3) {
      rep(j, 3) {
        char v = series_of_tik_tak_toe.at(t).at(i).at(j);
        if (v == 'o') {
          cnt++;
        }
      }
    }
  }

  cout << cnt << endl;
}