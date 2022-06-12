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

  int cnt = 0;
  int max_h = 0;
  rep(i, N) {
    int h;
    cin >> h;
    if (max_h <= h) {
      max_h = h;
      cnt++;
    }
  }

  cout << cnt << endl;
  return 0;
}
