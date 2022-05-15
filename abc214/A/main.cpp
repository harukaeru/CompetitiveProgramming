#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  if (1 <= N && N <= 125) {
    cout << 4 << endl;
  } else if (126 <= N && N <= 211) {
    cout << 6 << endl;
  } else {
    cout << 8 << endl;
  }
  return 0;
}
