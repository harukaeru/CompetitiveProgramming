#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  if (N % 2 == 0) {
    cout << N << endl;
    return 0;
  }

  cout << 2 * N << endl;
  return 0;
}
