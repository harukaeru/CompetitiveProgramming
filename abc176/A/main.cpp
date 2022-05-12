#include <bits/stdc++.h>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, X, T;
  cin >> N >> X >> T;

  int r = ceil((double)N / X);
  cout << r * T << endl;
  return 0;
}
