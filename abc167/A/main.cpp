#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  string t;
  cin >> s >> t;

  t.pop_back();

  cout << ((t == s) ? "Yes" : "No") << endl;
  return 0;
}