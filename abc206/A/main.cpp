#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;
  int result = (int)(N * 1.08);

  if (result < 206) {
    cout << "Yay!" << endl;
  } else if (result == 206) {
    cout << "so-so" << endl;
  } else {
    cout << ":(" << endl;
  }
  return 0;
}
