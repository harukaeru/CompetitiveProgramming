#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  vector<vector<string>> result(N, vector<string>(N, "-"));

  rep(i, M) {
    int a, b;
    cin >> a >> b;
    result.at(a - 1).at(b - 1) = "o";
    result.at(b - 1).at(a - 1) = "x";
  }

  rep(i, N) {
    rep(j, N) {
      cout << result.at(i).at(j);
      if (j != N - 1) {
        cout << " ";
      }
    }
    cout << endl;
  }

  return 0;
}
