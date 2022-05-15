#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int c = A - B;

  int ans = 1;
  while (c > 0) {
    ans *= 32;
    c--;
  }
  cout << ans << endl;
  return 0;
}
