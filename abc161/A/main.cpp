#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int X, Y, Z;
  cin >> X >> Y >> Z;
  swap(X, Y);
  swap(X, Z);

  cout << X << " " << Y << " " << Z << endl;

  return 0;
}
