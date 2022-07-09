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

  vector<long> L(N);
  rep(i, N) {
    cin >> L.at(i);
  }

  int cnt = 0;
  for (int i = 0; i < N - 2; i++) {
    long Li = L.at(i);
    for (int j = i + 1; j < N - 1; j++) {
      long Lj = L.at(j);
      for (int k = j + 1; k < N; k++) {
        long Lk = L.at(k);
        if (Li != Lj && Lj != Lk && Lk != Li) {
          long maxL = max({Li, Lj, Lk});
          long rest = Li + Lj + Lk - maxL;
          if (maxL < rest) {
            cnt++;
          }
        }
      }
    }
  }
  cout << cnt << endl;
  return 0;
}
