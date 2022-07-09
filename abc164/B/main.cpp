#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;

  int aoki_dead = (C + B - 1) / B;
  int takahashi_dead = (A + D - 1) / D;

  bool takahashi_win = takahashi_dead >= aoki_dead;

  if (takahashi_win) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
