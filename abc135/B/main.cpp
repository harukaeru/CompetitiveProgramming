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
  vector<int> p(N);
  rep(i, N) {
    cin >> p.at(i);
  }

  int diff_count = 0;
  rep(i, N) {
    int j = i + 1;
    if (p.at(i) != j) {
      diff_count++;
    }
  }

  if (diff_count <= 2) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}
