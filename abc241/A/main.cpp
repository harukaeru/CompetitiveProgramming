#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<int> vec(10);
  rep(i, 10) {
    cin >> vec.at(i);
  }

  int n = vec.at(0);
  n = vec.at(n);
  n = vec.at(n);

  cout << n << endl;
  return 0;
}
