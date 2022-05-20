#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, M, X;
  cin >> N >> M >> X;

  vector<int> block(N + 1);
  rep(i, M) {
    int j;
    cin >> j;
    block.at(j) = 1;
  }

  int cost_from_left = 0;
  for (int i = X; i > 0; i--) {
    if (block.at(i)) {
      cost_from_left++;
    }
  }

  int cost_from_right = 0;
  for (int i = X; i < N; i++) {
    if (block.at(i)) {
      cost_from_right++;
    }
  }
  // cout << "left: " << cost_from_left << endl;
  // cout << "right: " << cost_from_right << endl;

  cout << min(cost_from_left, cost_from_right) << endl;

  return 0;
}
