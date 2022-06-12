#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int f(int a) {
  return (a + 9) / 10 * 10;
}

int main() {
  int A, B, C, D, E;
  cin >> A >> B >> C >> D >> E;
  vector<int> v = {A, B, C, D, E};

  int min_t = 99999999;
  do {
    int t = f(f(f(f(v.at(0)) + v.at(1)) + v.at(2)) + v.at(3)) + v.at(4);
    min_t = min(min_t, t);

  } while (next_permutation(v.begin(), v.end()));

  cout << min_t << endl;

  return 0;
}
