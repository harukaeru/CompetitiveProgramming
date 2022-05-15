#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, A, X, Y;
  cin >> N >> A >> X >> Y;

  cout << min(N, A) * X + max(0, N - A) * Y << endl;

  return 0;
}
