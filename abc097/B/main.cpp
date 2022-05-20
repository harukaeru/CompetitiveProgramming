#include <bits/stdc++.h>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X;
  cin >> X;

  int max_v = 0;

  for (int b = 1; b < 32; b++) {
    for (int p = 2; p <= 10; p++) {
      int v = pow(b, p);

      if (X >= v) {
        max_v = max(max_v, v);
      }
    }
  }

  cout << max_v << endl;
  return 0;
}
