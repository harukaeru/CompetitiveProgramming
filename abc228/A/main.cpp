#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int S, T, X;
  cin >> S >> T >> X;

  if (S > T) {
    if (T <= X && X < S) {
      cout << "No" << endl;
    } else {
      cout << "Yes" << endl;
    }
  } else {

    if (S <= X && X < T) {
      cout << "Yes" << endl;
    } else {
      cout << "No" << endl;
    }
  }
  return 0;
}
