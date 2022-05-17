#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;
  set<int> s;
  rep(i, N) {
    int k;
    cin >> k;
    s.insert(k);
  }

  cout << s.size() << endl;

  return 0;
}
