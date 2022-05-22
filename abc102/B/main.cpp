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
  vector<int> A(N);
  rep(i, N) {
    cin >> A.at(i);
  }

  int ma = *max_element(A.begin(), A.end());
  int mi = *min_element(A.begin(), A.end());

  cout << abs(ma - mi) << endl;
  return 0;
}
