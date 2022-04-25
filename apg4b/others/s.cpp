#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  vector<int> A(3), B(3);

  rep(i, 3) {
    cin >> A.at(i);
  }

  rep(i, 3) {
    cin >> B.at(i);
  }

  bool found = false;

  rep(ai, 3) {
    int a = A.at(ai);

    rep(bi, 3) {
      int b = B.at(bi);

      if (a == b) {
        found = true;
        goto end_of_search;
      }
    }
  }

end_of_search:
  if (found) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}
