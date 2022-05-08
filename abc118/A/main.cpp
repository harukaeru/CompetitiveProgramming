#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  if (B % A == 0) {
    cout << A + B << endl;
  } else {
    cout << B - A << endl;
  }
  return 0;
}
