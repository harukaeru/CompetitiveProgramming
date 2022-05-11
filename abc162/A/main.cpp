#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string N;
  cin >> N;

  cout << ((count(N.begin(), N.end(), '7')) ? "Yes" : "No") << endl;

  return 0;
}
