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
  for (int i = 1; i < N; i++) {
    int cnt = 0;
    for (char c = 'a'; c <= 'z'; c++) {
      bool left = false, right = false;
      for (int j = 0; j < i; j++) {
        if (S.at(j) == c) {
          left = true;
        }
      }

      for (int j = i; j < N; j++) {
        if (S.at(j) == c) {
          right = true;
        }
      }
      if (left && right) {
        cnt++;
      }
    }

    m = max(m, cnt);
  }
  cout << m << endl;

  return 0;
}
