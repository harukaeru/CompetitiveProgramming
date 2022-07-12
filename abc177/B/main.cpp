#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  string S, T;
  cin >> S >> T;

  int min_count = 999999;
  for (int i = 0; i < (int)(S.size()) - (int)T.size() + 1; i++) {
    int count = 0;
    for (int j = 0; j < (int)(T.size()); j++) {
      char s = S.at(j + i);
      char t = T.at(j);
      if (s != t) {
        count++;
      }
    }
    min_count = min(min_count, count);
  }

  cout << min_count << endl;
  return 0;
}
