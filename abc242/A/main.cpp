#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;

  if (X <= A) {
    cout << 1.0 << endl;
    return 0;
  }
  if (B < X) {
    cout << 0.0 << endl;
    return 0;
  }

  cout << (C * 1.0) / (B - (A + 1) + 1) << endl;

  return 0;
}
