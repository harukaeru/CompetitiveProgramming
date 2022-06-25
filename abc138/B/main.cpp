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

  cout << setprecision(10);

  vector<int> A(N);
  rep(i, N) {
    cin >> A.at(i);
  }

  sort(A.begin(), A.end());

  double inv_ans = 0;
  rep(i, N) {
    inv_ans += 1.0 / A.at(i);
  }

  cout << 1.0 / inv_ans << endl;
  return 0;
}
