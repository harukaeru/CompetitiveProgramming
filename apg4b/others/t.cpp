#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  vector<vector<int>> data(3, vector<int>(4));

  rep(i, 3) {
    vector<int> vec = data.at(i);
    rep(j, 4) {
      cin >> data.at(i).at(j);
    }
  }

  int cnt = 0;

  rep(i, 3) {
    vector<int> vec = data.at(i);
    rep(j, 4) {
      if (vec.at(j) == 0) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;
}