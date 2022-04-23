#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  if (s.size() == 1) {
    cout << 1 << endl;
    return 0;
  }

  int result = 1;
  for (int i = 1; i < s.size(); i++) {
    if (i % 2 == 1) {
      if (s.at(i) == '+') {
        result += 1;
      } else {
        result -= 1;
      }
    }
  }

  cout << result << endl;

  return 0;
}
