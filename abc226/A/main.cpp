#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int a;
  char k;
  string b;
  cin >> a >> k >> b;
  int num = b.at(0) - '0';

  if (num >= 5) {
    cout << a + 1 << endl;
  } else {
    cout << a << endl;
  }

  return 0;
}
