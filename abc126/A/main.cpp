#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, K;
  string S;
  cin >> N >> K;
  cin >> S;

  S.at(K - 1) = tolower(S.at(K - 1));

  cout << S << endl;

  return 0;
}
