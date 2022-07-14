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

  int cnt = 0;
  rep(i, N) {
    int d1, d2;
    cin >> d1 >> d2;
    if (d1 == d2) {
      cnt++;
      if (cnt == 3) {
        cout << "Yes" << endl;
        return 0;
      }
    } else {
      cnt = 0;
    }
  }
  cout << "No" << endl;
  return 0;
}
