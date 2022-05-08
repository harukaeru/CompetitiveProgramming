#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int last_matched = (bool)(a <= b);

  cout << (a - 1) + last_matched << endl;

  return 0;
}
