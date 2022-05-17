#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, M;
  cin >> N;
  map<string, int> counter;

  rep(i, N) {
    string s;
    cin >> s;
    counter[s]++;
  }

  cin >> M;
  rep(i, M) {
    string s;
    cin >> s;
    counter[s]--;
  }

  int maximum = 0;
  for (auto &c : counter) {
    maximum = max(maximum, c.second);
  }

  cout << maximum << endl;

  return 0;
}
