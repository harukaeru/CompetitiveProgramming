#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int milk = A + B;
  if (milk >= 15 && B >= 8) {
    cout << 1 << endl;
    return 0;
  } else if (milk >= 10 && B >= 3) {
    cout << 2 << endl;
    return 0;
  } else if (milk >= 3) {
    cout << 3 << endl;
    return 0;
  }

  cout << 4 << endl;

  return 0;
}
