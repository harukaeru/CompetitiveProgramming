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

  int total = 0;
  int most_expensive = 0;

  rep(i, N) {
    int m;
    cin >> m;
    total += m;

    most_expensive = max(most_expensive, m);
  }

  cout << total - (most_expensive / 2) << endl;
  return 0;
}
