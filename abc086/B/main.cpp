#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;

  int n = stoi(a + b);

  for (int i = 1; i <= 2000; i++) {
    if (n == i * i) {
      cout << "Yes" << endl;
      return 0;
    }
  }

  cout << "No" << endl;

  return 0;
}
