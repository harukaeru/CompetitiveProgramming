#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;

  cin >> A >> B;

  bool is_even = (A % 2 == 0) || (B % 2 == 0);

  if (is_even) {
    cout << "No" << endl;
  } else {
    cout << "Yes" << endl;
  }
  return 0;
}
