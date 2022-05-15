#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  if (B < A) {
    cout << 0 << endl;
    return 0;
  }

  cout << B - A + 1 << endl;
  return 0;
}
