#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  int cnt = count(s.begin(), s.end(), 'o');

  cout << 700 + cnt * 100 << endl;
  return 0;
}
