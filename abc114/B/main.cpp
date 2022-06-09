#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  string S;
  cin >> S;

  int min_d = 999999;
  for (int i = 0; i < (int)S.size() - 2; i++) {
    string s = "";
    s.push_back(S.at(i));
    s.push_back(S.at(i + 1));
    s.push_back(S.at(i + 2));
    int c = stoi(s);
    min_d = min(abs(c - 753), min_d);
  }
  cout << min_d << endl;
  return 0;
}