#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  cout << fixed << setprecision(10) << 100 * (1 - (double)B / A) << endl;

  return 0;
}
