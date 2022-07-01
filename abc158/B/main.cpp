#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  long N, A, B;
  cin >> N >> A >> B;

  long r = N / (A + B);
  long rest = N % (A + B);

  cout << r * A + min(rest, A) << endl;
  return 0;
}
