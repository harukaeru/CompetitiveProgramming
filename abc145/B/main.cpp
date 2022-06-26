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
  string S;
  cin >> S;

  if (N % 2 != 0) {
    cout << "No" << endl;
    return 0;
  }

  string splitted = S.substr(0, N / 2);

  if (S == splitted + splitted) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
