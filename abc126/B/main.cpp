#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int main() {
  string s;
  cin >> s;

  string first = s.substr(0, 2);
  string second = s.substr(2, 2);

  set<string> month_set = {};
  for (int i = 1; i <= 12; i++) {
    if (i < 10) {
      string k = "0" + to_string(i);
      month_set.insert(k);
    } else {
      string k = to_string(i);
      month_set.insert(k);
    }
  }

  bool first_has_month = month_set.count(first);
  bool second_has_month = month_set.count(second);

  if (first_has_month && second_has_month) {
    cout << "AMBIGUOUS" << endl;
  } else if (first_has_month && !second_has_month) {
    cout << "MMYY" << endl;
  } else if (!first_has_month && second_has_month) {
    cout << "YYMM" << endl;
  } else if (!first_has_month && !second_has_month) {
    cout << "NA" << endl;
  }
  return 0;
}
