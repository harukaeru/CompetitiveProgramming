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

  int eight_dividable_count = 0;
  for (int n = 1; n <= N; n += 2) {
    int dividable_count = 0;
    for (int k = 1; k <= n; k++) {
      if (n % k == 0) {
        dividable_count++;
      }
    }
    if (dividable_count == 8) {
      eight_dividable_count++;
    }
  }

  cout << eight_dividable_count << endl;

  return 0;
}
