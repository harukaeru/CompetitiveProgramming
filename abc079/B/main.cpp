#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  vector<int64_t> L(100);

  L.at(0) = 2;
  L.at(1) = 1;
  for (int i = 2; i <= N; i++) {
    L.at(i) = L.at(i - 2) + L.at(i - 1);
  }

  cout << L.at(N) << endl;

  return 0;
}
