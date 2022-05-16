#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int f(int x) {
  return x * x + 2 * x + 3;
}

int main() {
  int t;
  cin >> t;

  cout << f(f(f(t) + t) + f(f(t))) << endl;
  return 0;
}
