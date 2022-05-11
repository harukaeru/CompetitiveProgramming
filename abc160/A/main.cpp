#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;

  cout << ((S.at(2) == S.at(3) && S.at(4) == S.at(5)) ? "Yes" : "No") << endl;
  return 0;
}
