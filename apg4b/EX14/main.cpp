#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  cout << max(max(A, B), C) - min(min(A, B), C) << endl;
  return 0;
}
