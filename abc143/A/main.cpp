#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int r = max(A - 2 * B, 0);

  cout << r << endl;
  return 0;
}
