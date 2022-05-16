#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int total = 0;

  rep(i, 9) {
    char c;
    cin >> c;
    total += (c - '0');
  }

  cout << 45 - total << endl;

  return 0;
}
