#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int calc_d2(vector<int> a, vector<int> b) {
  int total = 0;
  for (int i = 0; i < (int)a.size(); i++) {
    int c = a.at(i) - b.at(i);
    total += c * c;
  }
  return total;
}

int main() {
  set<int> d2_set;
  rep(i, 400) {
    int j = i + 1;
    d2_set.insert(j * j);
  }

  int N, D;
  cin >> N >> D;

  vector<vector<int>> vec;
  rep(i, N) {
    vector<int> x;
    rep(j, D) {
      int x_ij;
      cin >> x_ij;
      x.push_back(x_ij);
    }
    vec.push_back(x);
  }

  int cnt = 0;
  for (int i = 0; i < (int)vec.size() - 1; i++) {
    vector<int> x_left = vec.at(i);
    for (int j = i + 1; j < (int)vec.size(); j++) {
      vector<int> x_right = vec.at(j);
      int d2 = calc_d2(x_left, x_right);
      if (d2_set.count(d2)) {
        cnt++;
      }
    }
  }

  cout << cnt << endl;

  return 0;
}
