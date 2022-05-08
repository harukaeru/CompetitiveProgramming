#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int a, b, c, d;

  cin >> a >> b >> c >> d;

  if (abs(a - c) <= d) {
    cout << "Yes" << endl;
    return 0;
  }

  if (abs(a - b) <= d && abs(b - c) <= d) {
    cout << "Yes" << endl;

  } else {
    cout << "No" << endl;
  }
  return 0;
}