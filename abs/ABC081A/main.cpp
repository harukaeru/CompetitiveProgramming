#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;

  cin >> s;

  int cnt = 0;
  rep(i, s.size()) {
    if ('1' == s.at(i)) {
      cnt++;
    }
  }

  cout << cnt << endl;

  return 0;
}
