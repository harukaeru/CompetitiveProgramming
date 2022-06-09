#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N, M, X, Y;
  cin >> N >> M >> X >> Y;

  vector<int> x_pos(N);
  vector<int> y_pos(M);

  rep(i, N) {
    cin >> x_pos.at(i);
  }
  rep(i, M) {
    cin >> y_pos.at(i);
  }

  int max_x = *max_element(x_pos.begin(), x_pos.end());
  int min_y = *min_element(y_pos.begin(), y_pos.end());

  for (int z = X + 1; z <= Y; z++) {
    if (max_x < z && z <= min_y) {
      cout << "No War" << endl;
      return 0;
    }
  }

  cout << "War" << endl;

  return 0;
}
