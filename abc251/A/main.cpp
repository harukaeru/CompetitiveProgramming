#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;

  S = S + S + S + S + S + S;

  cout << S.substr(0, 6) << endl;
  return 0;
}
