#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {

  set<char> c_set;
  rep(i, 3) {
    char c;
    cin >> c;
    c_set.insert(c);
  }

  cout << ((c_set.size() == 1) ? "No" : "Yes") << endl;
  return 0;
}
