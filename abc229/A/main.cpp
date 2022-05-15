#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s1, s2;
  cin >> s1 >> s2;

  if (s1.at(0) == '#' && s2.at(1) == '#') {
    if (s1.at(1) == '.' && s2.at(0) == '.') {
      cout << "No" << endl;
      return 0;
    }
  }

  if (s1.at(1) == '#' && s2.at(0) == '#') {
    if (s1.at(0) == '.' && s2.at(1) == '.') {
      cout << "No" << endl;
      return 0;
    }
  }

  cout << "Yes" << endl;

  return 0;
}
