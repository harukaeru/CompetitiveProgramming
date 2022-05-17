#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;
  string S;
  cin >> S;
  rep(i, A + B + 1) {
    if (i >= (int)S.size()) {
      cout << "No" << endl;
      return 0;
    }

    if (i == A) {
      if (S.at(i) != '-') {
        cout << "No" << endl;
        return 0;
      }
    } else {
      int l = S.at(i) - '0';
      if (l < 0 || 9 < l) {
        cout << "No" << endl;
        return 0;
      }
    }
  }
  cout << "Yes" << endl;
  return 0;
}
