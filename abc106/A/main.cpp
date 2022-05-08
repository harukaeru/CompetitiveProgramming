#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int S = A * B;

  cout << S - A - B + 1 << endl;
  return 0;
}
