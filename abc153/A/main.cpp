#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int H, A;
  cin >> H >> A;

  int r = H / A;
  if (H % A != 0) {
    r++;
  }

  cout << r << endl;
  return 0;
}
