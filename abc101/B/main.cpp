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
  int originalN = N;

  int s = 0;
  while (0 < N) {
    s += N % 10;
    N /= 10;
  }

  if (s == 0) {
    cout << "No" << endl;
    return 0;
  }

  if (originalN % s == 0) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
