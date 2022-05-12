#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;

  int l = a.at(0) - '0' + a.at(1) - '0' + a.at(2) - '0';
  int r = b.at(0) - '0' + b.at(1) - '0' + b.at(2) - '0';

  cout << max(l, r) << endl;
  return 0;
}
