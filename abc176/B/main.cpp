#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  string N;
  cin >> N;

  int total = 0;
  rep(i, N.size()) {
    char c = N.at(i);
    int n = c - '0';
    total += n;
  }
  if (total % 9 == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
