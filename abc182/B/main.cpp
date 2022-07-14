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
  int max_a = -1;
  rep(i, N) {
    cin >> A.at(i);
    max_a = max(max_a, A.at(i));
  }

  int max_gcd_degree = -1;
  int ans = -1;
  for (int i = 2; i <= max_a; i++) {
    int gcd_degree = 0;
    for (int j = 0; j < (int)A.size(); j++) {
      if (A.at(j) % i == 0) {
        gcd_degree++;
      }
    }

    if (max_gcd_degree <= gcd_degree) {
      max_gcd_degree = gcd_degree;
      ans = i;
    }
  }

  cout << ans << endl;

  return 0;
}
