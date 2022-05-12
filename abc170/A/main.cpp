#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  rep(i, 5) {
    int s;
    cin >> s;
    if (s == 0) {
      cout << i + 1 << endl;
    }
  }

  return 0;
}
