#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<int> x(3);
  rep(i, 3) {
    cin >> x.at(i);
  }

  sort(x.begin(), x.end());

  cout << x.at(2) * 10 + x.at(1) + x.at(0) << endl;

  return 0;
}
