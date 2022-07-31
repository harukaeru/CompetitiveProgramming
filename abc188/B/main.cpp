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
  vector<int> B(N);
  rep(i, N) {
    cin >> A.at(i);
  }
  rep(i, N) {
    cin >> B.at(i);
  }

  int total = 0;
  rep(i, N) {
    total += A.at(i) * B.at(i);
  }

  if (total == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
