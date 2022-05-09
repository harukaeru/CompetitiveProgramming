#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C;
  cin >> A >> B >> C;

  cout << C - (min(B + C, A) - B) << endl;

  return 0;
}
