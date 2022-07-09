#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int K;
  cin >> K;

  string S;
  cin >> S;

  if ((int)(S.size()) <= K) {
    cout << S << endl;
  } else {
    cout << S.substr(0, K) << "..." << endl;
  }
  return 0;
}
