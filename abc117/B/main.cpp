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

  int max_l = 0;
  int s = 0;
  rep(i, N) {
    int l;
    cin >> l;
    max_l = max(l, max_l);
    s += l;
  }

  int total = s - max_l;

  if (total > max_l) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
