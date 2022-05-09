#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  if (A == B) {
    cout << 0 << endl;
    return 0;
  }

  if ((A + B) % 2 == 0) {
    cout << (A + B) / 2 << endl;
    return 0;
  }

  cout << "IMPOSSIBLE" << endl;

  return 0;
}
