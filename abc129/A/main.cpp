#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int P, Q, R;
  cin >> P >> Q >> R;
  cout << P + Q + R - max({P, Q, R}) << endl;

  return 0;
}
