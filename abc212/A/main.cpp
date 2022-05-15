#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;
  if (0 < A && B == 0) {
    cout << "Gold" << endl;
  } else if (0 == A && 0 < B) {
    cout << "Silver" << endl;
  } else {
    cout << "Alloy" << endl;
  }
  return 0;
}
