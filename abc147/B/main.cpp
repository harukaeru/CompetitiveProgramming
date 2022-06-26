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

  int N = (int)S.size();
  int cnt = 0;
  for (int i = 0; i < N / 2; i++) {
    if (S.at(i) != S.at(N - 1 - i)) {
      cnt++;
    }
  }
  cout << cnt << endl;

  return 0;
}
