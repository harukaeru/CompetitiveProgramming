#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;

  if (A < C) {
    cout << "Takahashi" << endl;
    return 0;
  } else if (A > C) {
    cout << "Aoki" << endl;
    return 0;
  }

  if (B <= D) {
    cout << "Takahashi" << endl;
    return 0;
  }

  cout << "Aoki" << endl;
  return 0;
}
