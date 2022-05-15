#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X;
  cin >> X;

  if (0 <= X && X < 40) {
    cout << 40 - X << endl;
  } else if (40 <= X && X < 70) {
    cout << 70 - X << endl;
  } else if (70 <= X && X < 90) {
    cout << 90 - X << endl;
  } else {
    cout << "expert" << endl;
  }
  return 0;
}
