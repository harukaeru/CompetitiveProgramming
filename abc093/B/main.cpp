#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, K;
  cin >> A >> B >> K;

  for (int i = A; i <= min(A + K - 1, B); i++) {
    cout << i << endl;
  }

  for (int i = max(A + K, B - K + 1); i <= B; i++) {
    cout << i << endl;
  }

  return 0;
}
