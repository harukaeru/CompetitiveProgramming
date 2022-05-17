#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  set<char> s;

  rep(i, N) {
    char c;
    cin >> c;

    s.insert(c);
  }

  if (s.size() == 3) {
    cout << "Three" << endl;
  } else {
    cout << "Four" << endl;
  }
  return 0;
}
