#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;
  int inc = count(S.begin(), S.end(), '+');
  int dec = count(S.begin(), S.end(), '-');

  cout << inc - dec << endl;
}
