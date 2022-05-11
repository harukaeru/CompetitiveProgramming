#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int K, A, B;
  cin >> K >> A >> B;

  int maximum = (B / K) * K;

  cout << ((maximum >= A) ? "OK" : "NG") << endl;

  return 0;
}
