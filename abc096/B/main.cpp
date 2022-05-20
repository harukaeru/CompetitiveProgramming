#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;
  int K;
  cin >> K;

  int m = max({A, B, C});
  int rest = A + B + C - m;

  m = m * (1 << K);

  cout << m + rest << endl;
  return 0;
}
