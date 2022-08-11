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
  int N;
  cin >> N;

  int found = false;
  int min_price = pow(10, 9) + 1;
  rep(i, N) {
    int a, p, x;
    cin >> a >> p >> x;

    int inventory = max(x - a, 0);
    if (inventory > 0) {
      found = true;
      min_price = min(min_price, p);
    }
  }

  if (!found) {
    cout << -1 << endl;
    return 0;
  }

  cout << min_price << endl;
  return 0;
}
