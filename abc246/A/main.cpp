#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int x1, y1;
  int x2, y2;
  int x3, y3;
  cin >> x1 >> y1;
  cin >> x2 >> y2;
  cin >> x3 >> y3;

  cout << (x1 ^ x2 ^ x3) << ' ' << (y1 ^ y2 ^ y3) << endl;

  return 0;
}
