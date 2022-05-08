#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, D;
  cin >> A >> B >> C >> D;

  cout << min(A, B) + min(C, D) << endl;

  return 0;
}
