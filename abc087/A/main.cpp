#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X, A, B;

  cin >> X >> A >> B;

  int r = X - A;

  cout << r % B << endl;
  return 0;
}
