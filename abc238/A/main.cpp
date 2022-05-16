#include <bits/stdc++.h>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

double log2(int n) {
  return log(n) / log(2);
}

int main() {
  int n;
  cin >> n;
  double m = 2 * log2(n);

  if (n > m) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  return 0;
}
