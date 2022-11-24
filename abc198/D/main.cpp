#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {

  string s1, s2, s3;
  cin >> s1 >> s2 >> s3;

  set<char> s;
  for (int i = 0; i < (int)s1.size(); i++) {
    s.insert(s1.at(i));
  }
  for (int i = 0; i < (int)s2.size(); i++) {
    s.insert(s2.at(i));
  }
  for (int i = 0; i < (int)s3.size(); i++) {
    s.insert(s3.at(i));
  }

  if (s.size() > 10) {
    cout << "UNSOLVABLE" << endl;
    return 0;
  }
  vector<char> v;
  int cnt = 10 - (int)s.size();
  v.assign(s.begin(), s.end());
  for (int i = 0; i < cnt; i++) {
    v.push_back('$' + i);
  }
  sort(v.begin(), v.end());

  do {
    string t1 = s1;
    string t2 = s2;
    string t3 = s3;

    for (int i = 0; i < 10; i++) {
      char x = v[i];
      char y = i + '0';
      replace(t1.begin(), t1.end(), x, y);
      replace(t2.begin(), t2.end(), x, y);
      replace(t3.begin(), t3.end(), x, y);
    }
    // cout << t1 << ' ' << t2 << ' ' << t3 << endl;
    if (t1[0] == '0' || t2[0] == '0' || t3[0] == '0') {
      continue;
    }
    if (stol(t1) + stol(t2) == stol(t3)) {
      cout << t1 << endl;
      cout << t2 << endl;
      cout << t3 << endl;
      return 0;
    }
  } while (next_permutation(v.begin(), v.end()));

  cout << "UNSOLVABLE" << endl;
  return 0;
}
