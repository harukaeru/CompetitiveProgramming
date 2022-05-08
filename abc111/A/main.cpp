#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  rep(i, s.size()) {
    if (s.at(i) == '1') {
      s.at(i) = 't';
    }
    if (s.at(i) == '9') {
      s.at(i) = '1';
    }
    if (s.at(i) == 't') {
      s.at(i) = '9';
    }
  }

  cout << s << endl;
}
