#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long A, B, K;
  cin >> A >> B >> K;

  long hungry = A - K;

  if (hungry >= 0) {
    cout << hungry << ' ' << B << endl;
    return 0;
  }

  if (hungry < 0) {
    long rest = B + hungry;
    if (B + hungry <= 0) {
      rest = 0;
    }
    cout << 0 << ' ' << rest << endl;
  }

  return 0;
}
