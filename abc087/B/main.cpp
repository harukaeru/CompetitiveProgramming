#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;

  int cnt = 0;
  rep(i, A + 1) {
    rep(j, B + 1) {
      int rest = X - (500 * i + 100 * j);
      if (rest % 50 == 0) {
        int c = rest / 50;
        if (0 <= c && c <= C) {
          cnt++;
        }
      }
    }
  }

  cout << cnt << endl;

  return 0;
}
