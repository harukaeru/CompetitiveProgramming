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

  rep(i, S.size()) {
    char s = S.at(i);

    if (i % 2 == 1) {
      if (!isupper(s)) {
        cout << "No" << endl;
        return 0;
      }
    } else {
      if (!islower(s)) {
        cout << "No" << endl;
        return 0;
      }
    }
  }

  cout << "Yes" << endl;
  return 0;
}
