#include <bits/stdc++.h>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define pp(v)              \
  for (auto x : v) {       \
    std::cout << x << ' '; \
  }                        \
  std::cout << endl;

int f(int n) {
  if (n % 2 == 0) {
    return n / 2;
  } else {
    return 3 * n + 1;
  }
}

int main() {
  int s;
  cin >> s;

  vector<int> a;
  for (int i = 0; i < 1000000; i++) {
    if (i == 0) {
      a.push_back(s);
    } else {
      a.push_back(f(a.at(i - 1)));
    }
  }

  set<int> done = {a.at(0)};

  for (int i = 1; i < (int)a.size(); i++) {
    int a_i = a.at(i);
    if (done.count(a_i)) {
      cout << i + 1 << endl;
      return 0;
    }
    done.insert(a_i);
  }

  return 0;
}
