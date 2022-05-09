#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  char c = '_';
  rep(i, s.size()) {
    if (s.at(i) == c) {
      cout << "Bad" << endl;
      return 0;
    }
    c = s.at(i);
  }

  cout << "Good" << endl;

  return 0;
}
