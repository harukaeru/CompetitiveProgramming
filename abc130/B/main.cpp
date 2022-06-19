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

  vector<int> L(N);
  rep(i, N) {
    cin >> L.at(i);
  }

  int current = 0;
  int cnt = 1;
  for (int i = 0; i < N; i++) {
    current = current + L.at(i);

    if (current <= X) {
      cnt++;
    }
  }

  cout << cnt << endl;

  return 0;
}
