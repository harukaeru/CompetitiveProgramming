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

  set<char> sc = {'A', 'C', 'G', 'T'};

  int max_cnt = 0;

  for (int i = 0; i < (int)S.size() - 1; i++) {
    int cnt = 0;
    if (sc.count(S.at(i))) {
      cnt++;
    }
    for (int j = i + 1; j < (int)S.size(); j++) {
      if (sc.count(S.at(j))) {
        cnt++;
      } else {
        break;
      }
    }
    if (max_cnt < cnt) {
      max_cnt = cnt;
    }
  }

  cout << max_cnt << endl;
  return 0;
}
