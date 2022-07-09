#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int A, B, C, K;
  cin >> A >> B >> C >> K;

  if (A >= K) {
    cout << K << endl;
    return 0;
  }

  K -= A;

  if (B >= K) {
    cout << A << endl;
    return 0;
  }

  K -= B;

  auto rest = min(C, K);

  cout << A - rest << endl;

  return 0;
}
