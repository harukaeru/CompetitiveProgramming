#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, L;
  cin >> N >> L;

  vector<int> vec;
  rep(i, N) {
    int v = L + (i + 1) - 1;
    vec.push_back(v);
  }

  int t = 0;
  int min_d = 9999999;
  int extracted = 9999999;
  rep(i, N) {
    int s = vec.at(i);
    t += s;

    if (min_d > abs(s)) {
      min_d = abs(s);
      extracted = s;
    }
  }

  cout << t - extracted << endl;

  return 0;
}
