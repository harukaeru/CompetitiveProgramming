#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  int maxi = B / C;
  if (A <= maxi * C && maxi * C <= B) {
    cout << maxi * C << endl;
  } else {
    cout << -1 << endl;
  }
  return 0;
}
