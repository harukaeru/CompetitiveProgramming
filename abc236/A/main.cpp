#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;
  int a, b;
  cin >> a >> b;

  swap(S.at(a - 1), S.at(b - 1));

  cout << S << endl;
  return 0;
}
