#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int ans = 0;
  if (A >= B) {
    ans += A;
    A--;
  } else {
    ans += B;
    B--;
  }

  ans += max(A, B);

  cout << ans << endl;

  return 0;
}
