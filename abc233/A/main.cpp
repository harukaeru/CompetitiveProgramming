#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X, Y;
  cin >> X >> Y;

  if (X >= Y) {
    cout << 0 << endl;
    return 0;
  }

  cout << (Y - X + 9) / 10 << endl;
  return 0;
}
