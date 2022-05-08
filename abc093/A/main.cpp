#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;

  cin >> S;

  sort(S.begin(), S.end());

  cout << ((S == "abc") ? "Yes" : "No") << endl;

  return 0;
}
