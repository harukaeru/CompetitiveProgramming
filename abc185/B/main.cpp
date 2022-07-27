#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M, T;
  cin >> N >> M >> T;
  vector<int> A(M);
  vector<int> B(M);
  rep(i, M) {
    cin >> A.at(i);
    cin >> B.at(i);
  }

  int battery = N;
  int current_time = 0;
  rep(i, M) {
    battery -= (A.at(i) - current_time);
    if (battery <= 0) {
      cout << "No" << endl;
      return 0;
    }
    battery = min(battery + (B.at(i) - A.at(i)), N);
    current_time = B.at(i);
  }

  battery -= T - B.at(M - 1);
  if (battery <= 0) {
    cout << "No" << endl;
    return 0;
  }

  cout << "Yes" << endl;

  return 0;
}
