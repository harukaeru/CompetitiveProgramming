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
  cin >> S;
  cin >> T;

  int d = 0;
  rep(i, S.size()) {
    char s_i = S.at(i);
    char t_i = T.at(i);
    if (s_i != t_i) {
      d++;
    }
  }
  cout << d << endl;
  return 0;
}
