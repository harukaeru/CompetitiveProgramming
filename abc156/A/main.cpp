#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, R;
  cin >> N >> R;

  if (N >= 10) {
    cout << R << endl;
    return 0;
  }

  cout << R + 100 * (10 - N) << endl;
  return 0;
}
