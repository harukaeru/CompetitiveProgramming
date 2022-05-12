#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  if (s.at(s.size() - 1) == 's') {
    cout << s + "es" << endl;
  } else {
    cout << s + "s" << endl;
  }
  return 0;
}
