#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, T;
  cin >> A >> B >> T;

  int cnt = (int)((T + 0.5) / A) * B;

  cout << cnt << endl;
  return 0;
}
