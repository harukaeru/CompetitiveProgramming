#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  const int N = 2000;
  int x = 0;
  rep(i, N) {
    rep(j, N) {
      cout << i + j << endl;
    }
  }

  rep(i, N) {
    cout << i << endl;
  }

  rep(i, N) {
    rep(j, N) {
      cout << i + j << endl;
    }
    rep(j, N) {
      cout << i + j << endl;
    }
    rep(j, N) {
      cout << i + j << endl;
    }
  }

  cout << x << endl;
}