#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;

  sort(S.begin(), S.end());

  bool is_same = (S.at(0) == S.at(1)) && (S.at(2) == S.at(3));
  bool is_different = S.at(0) != S.at(2);

  cout << ((is_same && is_different) ? "Yes" : "No") << endl;
  return 0;
}