#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i <= (int)(n); i++)

using namespace std;

int main() {
  int N, Y;
  cin >> N >> Y;

  rep(i, N) {
    rep(j, N - i) {
      int k = N - i - j;
      if (k < 0) {
        continue;
      }

      int candidate_total = 10000 * i + 5000 * j + 1000 * k;
      if (Y == candidate_total) {
        cout << i << " " << j << " " << k << endl;
        return 0;
      }
    }
  }

  cout << "-1 -1 -1" << endl;

  return 0;
}
