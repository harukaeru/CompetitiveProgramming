#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int T;
  int X;
  cin >> T >> X;

  double ans = (double)T / X;

  cout << fixed << setprecision(10) << ans << endl;

  return 0;
}
