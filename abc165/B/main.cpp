#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long long X;
  cin >> X;
  long long money = 100;

  int cnt = 0;
  while (X > money) {
    money += money / 100;
    // cout << "money: " << money << endl;
    cnt++;
  }

  cout << cnt << endl;

  return 0;
}
