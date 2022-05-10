#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  set x = {1, 2, 3};

  x.erase(A);
  x.erase(B);

  cout << *x.begin() << endl;

  return 0;
}
