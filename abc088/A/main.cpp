#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  int req = N % 500;
  if (req > A) {
    cout << "No" << endl;
  } else {
    cout << "Yes" << endl;
  }

  return 0;
}
