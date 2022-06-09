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

  double total = 0;
  rep(i, N) {
    double x;
    string u;
    cin >> x >> u;
    if (u == "JPY") {
      total += x;
    } else {
      total += x * 380000.0;
    }
  }

  cout << setprecision(8) << total << endl;
  return 0;
}
