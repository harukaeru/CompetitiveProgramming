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

  int idx = S.size() - 1;
  while (idx >= 0) {
    char last = S.at(S.size() - 1);
    S.pop_back();
    S = last + S;
    if (S == T) {
      cout << "Yes" << endl;
      return 0;
    }
    idx--;
  }
  cout << "No" << endl;

  return 0;
}
