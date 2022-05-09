#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<int> x(5);

  rep(i, 5) {
    cin >> x.at(i);
  }
  int k;
  cin >> k;

  int d = abs(*max_element(x.begin(), x.end()) - *min_element(x.begin(), x.end()));

  cout << ((d > k) ? ":(" : "Yay!") << endl;
  return 0;
}
