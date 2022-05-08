#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  if (N % K == 0) {
    cout << 0 << endl;
  } else {
    cout << 1 << endl;
  }
  return 0;
}
