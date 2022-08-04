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
  int X;
  cin >> N >> X;

  int X100 = X * 100;
  int total_al = 0;
  rep(i, N) {
    int V, P;
    cin >> V >> P;
    int al = V * P;
    total_al += al;
    if (total_al > X100) {
      cout << i + 1 << endl;
      return 0;
    }
  }
  cout << -1 << endl;
  return 0;
}
