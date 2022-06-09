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

  set<string> already_called;

  string prev_x;
  cin >> prev_x;
  already_called.insert(prev_x);

  for (int i = 2; i <= N; i++) {
    string x;
    cin >> x;

    if (already_called.find(x) != already_called.end()) {
      cout << "No" << endl;
      return 0;
    }
    already_called.insert(x);

    if (x.at(0) != prev_x.back()) {
      cout << "No" << endl;
      return 0;
    }

    prev_x = x;
  }

  cout << "Yes" << endl;
  return 0;
}
