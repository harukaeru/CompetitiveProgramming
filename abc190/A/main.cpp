#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  if (C) {
    if (A < B) {
      cout << "Aoki" << endl;
      return 0;
    }

    cout << "Takahashi" << endl;
    return 0;
  }

  if (A > B) {
    cout << "Takahashi" << endl;
    return 0;
  }

  cout << "Aoki" << endl;
  return 0;
}
