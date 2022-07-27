#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, X;
  string s;
  cin >> N >> X;
  cin >> s;

  for (auto c : s) {
    if (c == 'x') {
      if (X > 0) {
        X--;
      }
    } else if (c == 'o') {
      X++;
    }
  }
  cout << X << endl;
  return 0;
}
