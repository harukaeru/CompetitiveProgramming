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
  long s = 0;
  rep(i, N) {
    long a, b;
    cin >> a >> b;

    s += (b - a + 1) * (a + b) / 2;
  }

  cout << s << endl;
  return 0;
}
