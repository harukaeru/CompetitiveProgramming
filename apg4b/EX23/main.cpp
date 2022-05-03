#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  map<int, int> m;
  int max_count = 0;
  int n_which_is_mode = -1;

  rep(i, N) {
    int n;
    cin >> n;
    if (m.count(n)) {
      ++m.at(n);
    } else {
      m[n] = 1;
    }

    if (m.at(n) > max_count) {
      n_which_is_mode = n;
      max_count = m.at(n);
    }
  }

  cout << n_which_is_mode << " " << max_count << endl;

  return 0;
}
