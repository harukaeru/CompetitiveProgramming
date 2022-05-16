#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int V, A, B, C;
  cin >> V >> A >> B >> C;

  V = V % (A + B + C);

  if (V < A) {
    cout << 'F' << endl;
    return 0;
  }
  V -= A;

  if (V < B) {
    cout << 'M' << endl;
    return 0;
  }
  V -= B;

  if (V < C) {
    cout << 'T' << endl;
    return 0;
  }

  return 0;
}
