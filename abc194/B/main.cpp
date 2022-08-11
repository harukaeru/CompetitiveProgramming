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
    cin >> A.at(i) >> B.at(i);
  }

  int min_a = 99999999;
  int i_when_min_a = -1;

  int min_b = 99999999;
  int i_when_min_b = -1;

  for (int i = 0; i < N; i++) {
    int a = A.at(i);
    int b = B.at(i);

    if (min_a > a) {
      i_when_min_a = i;
      min_a = a;
    }
    if (min_b > b) {
      i_when_min_b = i;
      min_b = b;
    }
  }

  int min_total = 9999999;
  for (int i = 0; i < N; i++) {
    int a = A.at(i);
    int b = B.at(i);

    if (i != i_when_min_a) {
      min_total = min(min_total, max(min_a, b));
    } else {
      min_total = min(min_total, min_a + b);
    }
    if (i != i_when_min_b) {
      min_total = min(min_total, max(a, min_b));
    } else {
      min_total = min(min_total, a + min_b);
    }
  }

  cout << min_total << endl;
  return 0;
}
