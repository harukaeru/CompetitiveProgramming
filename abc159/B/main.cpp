#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

bool is_cycle(string &s) {
  int size = (int)s.size();
  bool is_same = true;
  for (int i = 0; i < size / 2; i++) {

    if (s.at(i) != s.at(size - 1 - i)) {
      is_same = false;
      return is_same;
    }
  }
  return is_same;
}

int main() {
  string S;
  cin >> S;

  int N = (int)S.size();
  string x = S.substr(0, (N - 1) / 2);
  string y = S.substr((N + 3) / 2 - 1, (N - 1) / 2);

  if (is_cycle(x) && is_cycle(y) && is_cycle(S)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
