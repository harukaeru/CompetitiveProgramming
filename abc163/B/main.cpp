#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M;
  cin >> N >> M;

  int t = 0;
  rep(i, M) {
    int a;
    cin >> a;
    t += a;
  }

  cout << max(N - t, -1) << endl;
  return 0;
}
