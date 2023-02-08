#include <bits/stdc++.h>
using namespace std;
#define mod 1000000009
#define N 21
int a[N][N];
long dp[N + 1][1 << N];

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> a[i][j];
    }
  }

  // memset(dp, 0, sizeof dp);
  dp[0][0] = 1;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < (1 << n); j++) {
      for (int k = 0; k < n; k++) {
        if (a[i][k] == 1 && (j & (1 << k)) == 0) {
          long nex = j | (1 << k);
          dp[i + 1][nex] += dp[i][j];
          dp[i + 1][nex] %= mod;
        }
      }
    }
  }

  cout << dp[n][(1 << n) - 1] << endl;
  return 0;
}
