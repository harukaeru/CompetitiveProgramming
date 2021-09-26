#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int MOD = 998244353;

  long n;
  cin >> n;

  std::vector<long> a;

  for(int i=0; i < n; i++){
       int x;
       std::cin >> x;
       a.push_back(x);
  }

  long dp[n][10];
  for(long i=0; i < n; i++){
    for(int j=0; j < 10; j++){
       dp[i][j] = 0;
    }
  }

  dp[0][a[0]] = 1;

  for(int i=0; i < n; i++){
      if (i == 0) {
          continue;
      }
    for(int j=0; j < 10; j++){
        long v = dp[i - 1][j];
        if (v > 0) {
            int aa = a[i] % 10;
            int p = (j + aa) % 10;
            int q = (j * aa) % 10;
            dp[i][p] += v % MOD;
            dp[i][q] += v % MOD;
        }
        // cout << dp[i][j] << endl;
    }

  }

  for(int i=0; i < 10; i++){
      cout << dp[n-1][i] % MOD << endl;
  }

  return 0;
}
