#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  int maxCount = 0;
  int cnt = 0;
  rep(i, 3) {
    if (s.at(i) == 'R') {
      cnt++;
      maxCount = max(maxCount, cnt);
    } else {
      cnt = 0;
    }
  }
  cout << maxCount << endl;

  return 0;
}
