#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, X;
  cin >> N >> X;
  rep(i, N) {
    int a;
    cin >> a;
    if (a == X) {
      continue;
    }

    cout << a;
    if (i != N - 1) {
      cout << ' ';
    }
  }
  cout << endl;

  return 0;
}
