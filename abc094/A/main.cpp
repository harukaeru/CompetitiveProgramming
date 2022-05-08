#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, X;
  cin >> A >> B >> X;

  if (A > X) {
    cout << "NO" << endl;
    return 0;
  }

  cout << ((A + B >= X) ? "YES" : "NO") << endl;

  return 0;
}
