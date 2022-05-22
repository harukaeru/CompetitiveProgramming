#include <bits/stdc++.h>
#include <math.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int D, N;
  cin >> D >> N;

  int x = pow(100, D);
  int ans = (N % 100 == 0) ? x * (N + 1) : x * N;

  cout << ans << endl;

  return 0;
}
