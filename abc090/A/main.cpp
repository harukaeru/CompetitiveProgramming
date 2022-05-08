#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<string> a;
  rep(i, 3) {
    string s;
    cin >> s;
    a.push_back(s);
  }

  cout << a.at(0)[0] << a.at(1)[1] << a.at(2)[2] << endl;
  return 0;
}
