#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<int> A(3);
  cin >> A.at(0) >> A.at(1) >> A.at(2);

  sort(A.begin(), A.end());

  if (A.at(1) - A.at(0) == A.at(2) - A.at(1)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
