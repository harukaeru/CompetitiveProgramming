#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  char a, b, c;
  cin >> a >> b >> c;

  cout << stoi(string({a, b, c})) + stoi(string({b, c, a})) + stoi(string({c, a, b})) << endl;
  return 0;
}
