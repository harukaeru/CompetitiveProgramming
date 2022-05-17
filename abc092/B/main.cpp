#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  int D, X;

  cin >> N >> D >> X;
  vector<int> A(N);
  rep(i, N) {
    cin >> A.at(i);
  }

  rep(i, N) {
    // aは日数シードみたいなもの
    int a = A.at(i);
    for (int j = 0; j < 100; j++) {
      int d = j * a + 1;
      if (d <= D) {
        X += 1;
      } else {
        break;
      }
    }
  }

  cout << X << endl;

  return 0;
}
