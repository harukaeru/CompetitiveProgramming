#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;

  if (S == "er") {
    cout << "er" << endl;
    return 0;
  }

  reverse(S.begin(), S.end());

  if (S.at(0) == 'r' && S.at(1) == 'e') {
    cout << "er" << endl;
  } else if (S.at(0) == 't' && S.at(1) == 's' && S.at(2) == 'i') {
    cout << "ist" << endl;
  }

  return 0;
}
