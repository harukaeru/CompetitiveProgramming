#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {

  set<int> x;

  rep(i, 3) {
    int j;
    cin >> j;
    x.insert(j);
  }

  cout << ((x.size() == 2) ? "Yes" : "No") << endl;
  return 0;
}
