#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  cout << max({A + B, A - B, A * B}) << endl;
  return 0;
}
