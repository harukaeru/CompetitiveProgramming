#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;

  int left = A + B;
  int right = C + D;
  if (left > right) {
    cout << "Left" << endl;
  } else if (left == right) {
    cout << "Balanced" << endl;
  } else {
    cout << "Right" << endl;
  }
  return 0;
}
