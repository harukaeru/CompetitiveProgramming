#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N;
  cin >> N;

  vector<tuple<string, int, int>> vec(N);
  rep(i, N) {
    string s;
    int p;

    cin >> s >> p;

    vec.at(i) = make_tuple(s, -p, i + 1);
  }

  sort(vec.begin(), vec.end());

  rep(i, vec.size()) {
    cout << get<2>(vec.at(i)) << endl;
  }
  return 0;
}
