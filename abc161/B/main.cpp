#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(N);
  int total = 0;
  rep(i, N) {
    cin >> A.at(i);
    total += A.at(i);
  }

  int t = (total + 4 * M - 1) / (4 * M);

  int cnt = 0;
  rep(i, N) {
    int a = A.at(i);
    if (t <= a) {
      cnt++;
    }
  }

  if (M <= cnt) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
