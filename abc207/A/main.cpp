#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  cout << max({A + B, B + C, C + A}) << endl;
  return 0;
}
