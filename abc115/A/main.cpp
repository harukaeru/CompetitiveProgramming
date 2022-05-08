#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int D;
  cin >> D;

  if (D == 25) {
    cout << "Christmas" << endl;
  } else if (D == 24) {
    cout << "Christmas Eve" << endl;
  } else if (D == 23) {
    cout << "Christmas Eve Eve" << endl;
  } else if (D == 22) {
    cout << "Christmas Eve Eve Eve" << endl;
  }

  return 0;
}
