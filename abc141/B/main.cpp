#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  set<char> o = {'R', 'U', 'D'};
  set<char> e = {'L', 'U', 'D'};

  string S;
  cin >> S;

  rep(i, S.size()) {
    int s = S.at(i);
    if (i % 2 != 0) {
      if (!(e.count(s))) {
        cout << "No" << endl;
        return 0;
      }
    } else {
      if (!(o.count(s))) {
        cout << "No" << endl;
        return 0;
      }
    }
  }

  cout << "Yes" << endl;
  return 0;
}
