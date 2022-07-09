#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  int N;
  cin >> N;

  map<string, int> m;
  rep(i, N) {
    string s;
    cin >> s;
    m[s]++;
  }

  cout << "AC x " << m["AC"] << endl;
  cout << "WA x " << m["WA"] << endl;
  cout << "TLE x " << m["TLE"] << endl;
  cout << "RE x " << m["RE"] << endl;

  return 0;
}
