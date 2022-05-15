#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X, Y;
  char k;
  cin >> X >> k >> Y;

  if (0 <= Y && Y <= 2) {
    cout << X << '-' << endl;
  } else if (3 <= Y && Y <= 6) {
    cout << X << endl;
  } else {
    cout << X << '+' << endl;
  }

  return 0;
}
