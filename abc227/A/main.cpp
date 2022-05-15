#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, K, A;
  cin >> N >> K >> A;

  int adv = (K - 1) % N;
  cout << (A + adv - 1) % N + 1 << endl;
  return 0;
}
