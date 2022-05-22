#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  string S;
  cin >> S;

  if (S.at(0) != 'A') {
    cout << "WA" << endl;
    return 0;
  }

  S.at(0) = 'a';

  bool found = false;
  for (int i = 2; i < (int)S.size() - 1; i++) {
    if (S.at(i) == 'C') {
      if (found) {
        cout << "WA" << endl;
        return 0;
      }
      found = true;
      S.at(i) = 'c';
    }
  }

  if (!found) {
    cout << "WA" << endl;
    return 0;
  }

  rep(i, S.size()) {
    bool is_lower = false;
    for (char x = 'a'; x <= 'z'; x++) {
      if (S.at(i) == x) {
        is_lower = true;
        break;
      }
    }

    if (!is_lower) {
      cout << "WA" << endl;
      return 0;
    }
  }

  cout << "AC" << endl;

  return 0;
}
