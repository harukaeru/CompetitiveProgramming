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
  vector<int> C(N - 1);
  rep(i, N) {
    cin >> A.at(i);
  }
  rep(i, N) {
    cin >> B.at(i);
  }
  rep(i, N - 1) {
    cin >> C.at(i);
  }

  int s = 0;
  int prev_j = -99;
  rep(i, N) {
    int j = A.at(i) - 1;
    s += B.at(j);

    if (prev_j + 1 == j) {
      s += C.at(j - 1);
    }
    prev_j = j;
  }

  cout << s << endl;
  return 0;
}
