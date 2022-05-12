#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string C;
  cin >> C;

  set<char> ss;
  ss.insert(C.at(0));
  ss.insert(C.at(1));
  ss.insert(C.at(2));

  if (ss.size() == 1) {
    cout << "Won" << endl;
  } else {
    cout << "Lost" << endl;
  }
  return 0;
}
