#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int R;
  cin >> R;

  if (R < 1200) {
    cout << "ABC" << endl;
  } else if (R < 2800) {
    cout << "ARC" << endl;
  } else {
    cout << "AGC" << endl;
  }
  return 0;
}
