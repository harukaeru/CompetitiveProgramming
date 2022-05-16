#include <bits/stdc++.h>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int H;
  cin >> H;
  long long d = (12800000 + H);

  cout << fixed << setprecision(10) << sqrt(d) * sqrt(H) << endl;
  return 0;
}
