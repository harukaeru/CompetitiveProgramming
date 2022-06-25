#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int A, B;
  cin >> A >> B;

  if (B == 1) {
    cout << 0 << endl;
    return 0;
  }

  int n = ((B - A) + (A - 1) - 1) / (A - 1);
  cout << n + 1 << endl;

  return 0;
}
