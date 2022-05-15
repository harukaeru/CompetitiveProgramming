#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S;
  cin >> S;
  sort(S.begin(), S.end());

  int ans = 0;
  do {
    ans++;
  } while (next_permutation(S.begin(), S.end()));

  cout << ans << endl;

  return 0;
}
