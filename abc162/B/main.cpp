#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long N;
  cin >> N;

  long t = 0;
  for (long i = 1; i <= N; i++) {
    if (i % 5 == 0 || i % 3 == 0) {
      continue;
    }
    t += i;
  }
  cout << t << endl;
  return 0;
}
