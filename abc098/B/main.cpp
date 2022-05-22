#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

set<char> get_set(string s) {
  set<char> r;
  rep(i, s.size()) {
    r.insert(s.at(i));
  }
  return r;
}

int main() {
  int N;
  string S;
  cin >> N >> S;

  int m = 0;
  // カット位置
  for (int i = 1; i < N - 1; i++) {
    string left = S.substr(0, i);
    string right = S.substr(i, N - i);

    auto l = get_set(left);
    auto r = get_set(right);
    set<char> c;

    set_intersection(l.begin(), l.end(), r.begin(), r.end(), inserter(c, c.begin()));

    m = max(m, (int)c.size());
  }
  cout << m << endl;

  return 0;
}
