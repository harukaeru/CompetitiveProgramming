#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int K;
  cin >> K;

  int o, e;
  if (K % 2 == 0) {
    o = K / 2;
    e = K / 2;
  } else {
    o = K / 2 + 1;
    e = K / 2;
  }

  cout << o * e << endl;
  return 0;
}
