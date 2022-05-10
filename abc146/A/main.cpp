#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string s;
  cin >> s;

  vector<string> d = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

  auto it = find(d.begin(), d.end(), s);

  auto r = d.end() - it;
  cout << (int)r << endl;

  return 0;
}
